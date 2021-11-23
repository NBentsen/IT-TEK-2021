from machine import Pin
import neopixel #Indbygget bibliotek i Micropython, specielt lavet til Neopixel-ringe
import time
import random 

PIN_21 = Pin(21, Pin.OUT) #Her "åbner" vi for 3.3 på en ADC Pin.
PIN_21.value(1) #Her tænder vi for 3.3V

n = 12 #Her definere vi antallet af LED'er i ringen
p = 15 #Her definere vi pin, som vi sender signal til.

np = neopixel.NeoPixel(Pin(p), n) #Her laver vi variablen "np", som er en sammenlægning af signal Pin & antal LED'er

def clear(): #Rydder værdierne i de 12 LED'er - "slukker LED ring"
    for i in range(n): #For spændet i LED-ring"
        np[i] = (0, 0, 0) #Clearer værdierne i LEDerne
        np.write() #Eksekvere funktionen.

def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b) 
        np.write()
