from machine import Pin
import neopixel
import time
import random 

PIN_21 = Pin(21, Pin.OUT)
PIN_21.value(1)

n = 12
p = 15

np = neopixel.NeoPixel(Pin(p), n)

def clear():
    for i in range(n):
        np[i] = (0, 0, 0) 
        np.write() 

def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b) 
        np.write()
