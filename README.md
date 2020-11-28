# Pi-Sensor
This is a simple python script to grab sensor values from a DHT-22 sensor on Raspberry pi GPIO and send them over mqtt.
It was written to be used along with Home Assistant but really anything hooked into MQTT will work, but that is where the
state and availibity topic pattern comes from.

## Install and Config
I would encourage using basic best venv practices so you should be able to just install requirements on a fresh venv.


`pip install -r requirements.txt`


A sample config is provided just drop one similar with your values as `config.yaml` in the base dir. You may add `mqtt_port`
if your mqtt server is listening on the non standard port, without one it will use the default in the mqtt library.


## Usage
Since this is meant to be a long running process I tend to start it over ssh, don't forget to activate your venv before starting.

`nohup python3 main.py &!`
