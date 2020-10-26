import Adafruit_DHT

SENSOR = Adafruit_DHT.DHT22
PIN = 4

while True:
    humidity, temp = Adafruit_DHT.read_retry(SENSOR, PIN)

    if humidity is None:
        continue

    temp = (temp * 9/5) + 32
    print(f'Humidity {humidity}')
    print(f'Temp {temp}')


