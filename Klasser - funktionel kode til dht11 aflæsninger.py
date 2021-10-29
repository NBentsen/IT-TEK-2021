from machine import Pin
import dht
from time import sleep

sensor = dht.DHT11(Pin(14))


class sensor_class:
    description = "Class to store temp and hum"
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
    def set_temperature(self, measured_val: int):
        self.temperature = measured_val
    def set_humidity(self, measured_val : int):
        self.humidity = measured_val

print(sensor_class.description)
mysensor = sensor_class()
def dht11Temp():
    dht11Sensor = dht.DHT11(Pin(14))
    sleep(2)
    dht11Sensor.measure()
    return dht11Sensor.temperature()

def dht11Hum():
    dht11Sensor = dht.DHT11(Pin(14))
    sleep(2)
    dht11Sensor.measure()
    return dht11Sensor.humidity()

mysensor.set_temperature(dht11Temp())
mysensor.set_humidity(dht11Hum())
def my_func():
    print("Measured temp:", mysensor.temperature)
    print("Measured hum:", mysensor.humidity)

my_func()