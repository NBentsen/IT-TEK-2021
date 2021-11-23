import umqtt_robust2
import GPSfunk
import sved #Importere eget biblioteket "sved.py"
import Neopixel_debugging #Importere eget bibliotek "Neopixel_debugging.py"
from machine import Pin
from time import sleep_ms, sleep
from Vibrator import * # "*" Henter ALT hvad biblioteket "vibrator.py" indeholder.

lib = umqtt_robust2 #Vi "forkorter" umqtt_robust2 til lib, så det er mere overskueligt at kalde bibliotekets funktioner.
mapFeed = bytes('{:s}/feeds/{:s}'.format(b'NBentsen', b'mapfeed/csv'), 'utf-8')
speedFeed = bytes('{:s}/feeds/{:s}'.format(b'NBentsen', b'speedfeed/csv'), 'utf-8')
svedbanken = bytes('{:s}/feeds/{:s}'.format(b'NBentsen', b'svedbanken'), 'utf-8')

while True: #Så længe dette er sandt sker følgende:
    if lib.c.is_conn_issue(): #Hvis vi har forbindelses-problemer til 4G/Wifi sker:
        while lib.c.is_conn_issue(): #Imens det står på:
            Neopixel_debugging.set_color(255, 0, 0) #Sætter Neopixel-ring til rød.
            # hvis der forbindes returnere is_conn_issue metoden ingen fejlmeddelse
            lib.c.reconnect() #Genetablere forbindelse til 4G/Wifi
            print("reconnect") #Printer "reconnect" i rebel for sanity-check
        else:
            lib.c.resubscribe() #Går det  ikke, prøver den igen
            print('resubscribe') #Endnu et sanity-check
    try: #Når/Hvis den opretter forbindelse prøver den at:
        lib.c.publish(topic=mapFeed, msg=GPSfunk.main()) #Uploader GPSfunk-funktionen til Adafruit
        speed = GPSfunk.main()
        speed = speed[:4]
        print("speed: ",speed)
        lib.c.publish(topic=speedFeed, msg=speed) #Uploader Speedfeed
        print(type(sved.svedfunk()))
        sveddata = str(sved.svedfunk()) #Vi definere "Svedfunk"-funktionen som
                                        #en string, så Adafruit kan bruge værdierne til en graf
        lib.c.publish(topic=svedbanken, msg=sveddata) #Her uploader den sveddata til "Svedbanken"
        Neopixel_debugging.set_color(000, 255, 000) #Hvis alting afvikles korrekt, sæt LED-ring til grøn
        sleep(2) #Powernapper 2 sek
        
        ################ VIBRATOR START#####################
        ##SVE1_VIB##
        vib_currentTime = time.ticks_ms() #Her definere vi vibratorens tid til at være i ticks i millisekunder.
        if(sve1_runner == True and vib_currentTime - vib_prev_time > vib_interval): #WE NEED KEVIN!!!!!!
            vib_prev_time = vib_currentTime
            print("sve1_counter", sve1_counter, "vib_state", vib_state)
            if(vib_state == 1):
                vib_state = 0
                print("sætter state til 0")
            else:
                print("sætter state til 1")
                vib_state = 1
            vib.value(vib_state)
            vib_start_time = time.ticks_ms()
            sve1_counter +=1
        
            if sve1_counter > 11:
                sve1_runner = False
                sve1_counter = 0
            
                
        sve1_currentTime = time.ticks_ms()
        if(sved.svedfunk() >= 3000 and sved.svedfunk() < 3300 and  sve1_currentTime - sve1_prev_time > sve1_interval):  
            sve1_prev_time = sve1_currentTime
            sve1 +=1
            print(sve1)
        
        if(sve1 == 5):
            sve1 = 0
            sve1_runner = True
        
        ##SVE2_VIB##

        vib_currentTime = time.ticks_ms() #
        if(sve2_runner == True and vib_currentTime - vib_prev_time > vib_interval):  
            vib_prev_time = vib_currentTime
            print("sve2_counter", sve2_counter, "vib_state", vib_state)   
            vib2.value(vib_state)
            vib_start_time = time.ticks_ms()
            sve2_counter +=1
        
        if sve2_counter > 5:
            sve2_runner = False
            sve2_counter = 0
        

        sve2_currentTime = time.ticks_ms()
        if(sved.svedfunk() >= 3301 and sved.svedfunk() < 3316 and  sve2_currentTime - sve2_prev_time > sve2_interval):  
            sve2_prev_time = sve2_currentTime
            sve2 +=1
            print(sve2)
        
        if(sve2 == 5):
            sve2 = 0
            sve2_runner = True
    
        if(sve2_counter >= 1):
            vib2.value(1)
            
    ############VIBRATOR SLUT####################
        
    except KeyboardInterrupt: #Når Ctrl + C er trykket sker følgende:
        print('Ctrl-C pressed...exiting')
        Neopixel_debugging.set_color(255, 0, 0) #Sætter LED-ring rød
        lib.c.disconnect() #Disconnecter fra umqtt_robust2
        lib.wifi.active(False) #Slukker for Wifi
        lib.sys.exit() #Exitter systemet
    except OSError as e:
        print('Failed to read sensor.')
    except NameError as e:
        print('NameError', e)
    except TypeError as e:
        print('TypeError')
    lib.c.check_msg() #Checker om der er beskeder der skal sendes/modtages
    lib.c.send_queue() #Checker om der ligger beskeder i kø efter et evt. DC/Bottlenecking

lib.c.disconnect() #Skulle der ske bitflips eller lignede der bryder While-true løkken - stopper vi afvikling og sætter LED til Rød
Neopixel_debugging.set_color(255, 0, 0)
