import json
import time

import Adafruit_DHT
import paho.mqtt.client as mqtt
import yaml

SENSOR = Adafruit_DHT.DHT22

def load_config:
    with open('config.yml') as config:
        return yaml.load(config, Loader=yaml.Loader)

config = load_config()

availability_topic = config['availability_topic']
state_topic = config['state_topic']

def on_connect(client, userdata, flags, rc):
    client.publish(availability_topic, payload='Online', retain=True)

client = mqtt.Client()
client.username_pw_set(config['mqtt_user'], password=config['mqtt_password'])
client.on_connect = on_connect
client.will_set(availability_topic, payload='Offline')

connect_kwargs = {}
if 'mqtt_port' in config:
    connect_kwargs['port'] = config['mqtt_port']

client.connect(config['mqtt_server'], **connect_kwargs)
client.loop_start()

while True:
    humidity, temp = Adafruit_DHT.read_retry(SENSOR, config['pin'])

    if humidity is None:
        continue

    temp = (temp * 9/5) + 32
    payload = {
        'temp': round(temp, 1),
        'humidity': round(humidity, 1)
    }

    client.publish(state_topic, payload=json.dumps(payload), retain=True)

    time.sleep(15)
