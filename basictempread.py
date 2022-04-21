import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

pin = 2

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C ({1:0.1f}*F)  Humidity={2:0.1f}%'.format(temperature, (temperature * 1.8) + 32, humidity))
else:
    print('Failed to get reading. Try again!')
