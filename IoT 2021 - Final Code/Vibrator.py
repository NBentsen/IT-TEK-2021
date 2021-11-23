from time import sleep, ticks_ms #Vi importere ticks_ms i stedet for sleep for at
                                 #kunne sætte vores egne tids-variabler og
                                 #eksvere flere dele kode sideløbbende
from machine import Pin, ADC, PWM #PMW = Pulse With Modulation -
                                  #Bliver ikke brugt, men kan bruges til at styre styrken vibrationen
import machine
import sved #Fra et tidligere "build", inden Vibrator.py kun holdte variabler
            #Den bliver brugt i main i stedet
import time

##########VIBRATOR##########
vib = Pin(4, Pin.OUT)  #Vib & Vib2 er de 2 forskellige vibrationsmønstre -
                       #Det er ikke elegant kode, men den virker - kan helt sikkert optimeres.
vib2 = Pin(4, Pin.OUT)
vib2.value(0) #Sætter vibrator til "slukket" tilstand indtil vi kalder den

VIB_STROM = Pin(27, Pin.OUT) #Strømpin - giver muligheden for 3.3V ud af Pin27
VIB_STROM.value(1) #Sætter strømpin til at levere 3.3V
 
vib_prev_time = 0 #Sætter base-time til 0 på første vibrationsmønster
vib_interval = 1000 #Sætter intervalet til 1000ms(1sekund)
vib_state = 0 #Sætter vibratorens stadie til slukket

vib_prev_time2 = 0 #Sætter base-time på andet vibrationsmønster til 0
vib_interval2 = 800 #Sætter intervalet til 800ms(0.8 sekund)
vib_state2 = 0 #Sætter vibratorens andet vibrationsmøster-stadie til slukket

##########SVED_COUNT########
sve1 = 0 #Variablerne der indgår i de 2 vibrationsmønstres non-blocking delays.
sve1_counter = 0 #Vi starter en counter der med en start værdi på 0
sve1_runner = False #Vi sætter sve1/sve2_runner til False så den ikke afvikler funktionen før den har en "True" værdi
sve1_prev_time = 0 #Vi sætter tids-udgangspunktet til 0
sve1_interval = 1000 #Interval bliver sat til 1000 millisekunder(1 sekund)
sve1_state = 0 #Sve1/Sve2_state er sat til slukket


sve2 = 0
sve2_counter = 0
sve2_runner = False
sve2_prev_time = 0
sve2_interval = 1000
sve2_state = 0


##########ADC_PINS##########
adc = machine.ADC(machine.Pin(36)) #Trækker ADC målinger fra jordfugtighedsmåler.