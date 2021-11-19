from time import sleep, ticks_ms
from machine import Pin, ADC, PWM
import machine
import sved
import time

##########VIBRATOR##########
vib = Pin(4, Pin.OUT)
vib2 = Pin(4, Pin.OUT)
vib2.value(0)

VIB_STROM = Pin(27, Pin.OUT)
VIB_STROM.value(1)

vib_prev_time = 0
vib_interval = 1000
vib_state = 0

vib_prev_time2 = 0
vib_interval2 = 800
vib_state2 = 0

##########SVED_COUNT########
sve1 = 0
sve1_counter = 0
sve1_runner = False
sve1_prev_time = 0
sve1_interval = 1000
sve1_state = 0


sve2 = 0
sve2_counter = 0
sve2_runner = False
sve2_prev_time = 0
sve2_interval = 1000
sve2_state = 0


##########ADC_PINS##########
adc = machine.ADC(machine.Pin(36))