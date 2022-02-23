from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread

class Servo1Stat:
    servomax = 75
    servomin = 48
    servonorm = 48
    hastighed = 100
    joystickmeasurement = 2048
    joystickmax = 2100
    joystickmin = 1700
    servooption = False

def Servo1():

    servo1=PWM(Pin(23),freq=50)
    servo1.duty(Servo1Stat.servonorm)
    check = Servo1Stat.servooption
    i = Servo1Stat.servonorm
    while(check == True):
        sleep_ms(int(100))
        check = Servo1Stat.servooption
        y = int(Servo1Stat.joystickmeasurement)
        sleep(1)
        if(int(y) <= int(Servo1Stat.joystickmin)):
            while(i > Servo1Stat.servomin and y <= Servo1Stat.joystickmin and check == True):
                check = Servo1Stat.servooption
                y = int(Servo1Stat.joystickmeasurement)
                print("servo 1,1")
                servo1.duty(i)
                i = i - 1
                sleep_ms(Servo1Stat.hastighed)
        if(y >= int(Servo1Stat.joystickmax)):
            while(i < Servo1Stat.servomax and y >= Servo1Stat.joystickmax and check == True):
                check = Servo1Stat.servooption
                y = int(Servo1Stat.joystickmeasurement)
                print("servo 1,1")
                servo1.duty(i)
                i = i + 1
                sleep_ms(Servo1Stat.hastighed)