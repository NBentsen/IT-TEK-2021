from time import sleep
from machine import Pin, ADC
import machine

PIN_32 = Pin(32, Pin.OUT)
PIN_32.value(1)

adc = machine.ADC(machine.Pin(36))

def svedfunk():
        sveden = 0.81 * adc.read()
        print(sveden)
        sleep(1)
        return sveden
