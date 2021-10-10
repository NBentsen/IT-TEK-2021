from machine import Pin, PWM
from random import randint
r = PWM(Pin(18))
g = PWM(Pin(5))
b = PWM(Pin(19))
def newColor():
    print("New color!")
    r.duty(randint(0, 1023))
    g.duty(randint(0, 1023))
    b.duty(randint(0, 1023))
newColor()
