from time import sleep 
from machine import Pin, ADC
import machine #Importere al funktionalitet på ESP32

PIN_32 = Pin(32, Pin.OUT) #Her "åbner" vi for 3.3 på en ADC Pin.
PIN_32.value(1) #Her tænder vi for 3.3V

adc = machine.ADC(machine.Pin(36))
#Her definere vi vores jordfugtighedsmåler til Pin 36, så vi kan
#aflæse et analog input i 12BIT format

def svedfunk(): #Svedfunk er vores konverteringsformel fra 0-4095
                #bits til 001-3300 millivolt
        sveden = 0.81 * adc.read()
        print(sveden)
        sleep(1)
        return sveden #Return returnere formelen for varibalen
        #"sveden", så vi kan kalde funktionen igen og igen, derved skabe et "loop"
