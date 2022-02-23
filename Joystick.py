from time import sleep, sleep_ms
from machine import ADC, Pin
import sendingdata

def Joystick1x():
    joy1x = ADC(Pin(34))
    joy1x.atten(ADC.ATTN_11DB)
    joy1x.width(ADC.WIDTH_12BIT)
    while(True):
        measurement = joy1x.read()
        besked = "x1" + str(measurement)
        sendingdata.SendData(besked)
def Joystick1y():
    joy1y = ADC(Pin(39))
    joy1y.atten(ADC.ATTN_11DB)
    joy1y.width(ADC.WIDTH_12BIT)
    while(True):
        measurement = joy1y.read()
        besked = "y1" + str(measurement)
        sendingdata.SendData(besked)
def Joystick1b():
    joy1b = ADC(Pin(36))
    joy1b.atten(ADC.ATTN_11DB)
    joy1b.width(ADC.WIDTH_12BIT)
    while(True):
        measurement = joy1b.read()/4095
        if(measurement == 1):
            besked = "b1" + str(measurement)
            sendingdata.SendData(besked)
# def Joystick2x():
#     joy2x = ADC(Pin(33))
#     joy2x.atten(ADC.ATTN_11DB)
#     joy2x.width(ADC.WIDTH_12BIT)
#     while(True):
#         measurement = joy2x.read()
#         besked = "y2" + str(measurement)
#         sendingdata.SendData(besked)
# def Joystick2y():
#     joy2y = ADC(Pin(32))
#     joy2y.atten(ADC.ATTN_11DB)
#     joy2y.width(ADC.WIDTH_12BIT)
#     while(True):
#         measurement = joy2y.read()
#         besked = "y2" + str(measurement)
#         sendingdata.SendData(besked)
# def Joystick2b():
#     joy2b = ADC(Pin(35))
#     joy2b.atten(ADC.ATTN_11DB)
#     joy2b.width(ADC.WIDTH_12BIT)
#     while(True):
#         measurement = joy2b.read()/4095
#         if(measurement == 1):
#             besked = "b2" + str(measurement)
#             sendingdata.SendData(besked)
