import time
from machine import TouchPad, Pin

r_led = Pin(17, Pin.OUT)
r_prev_time = 0
r_interval = 100
r_state = 0
r = TouchPad(Pin(27))

g_led = Pin(1, Pin.OUT)
g_prev_time = 0
g_interval = 100
g_state = 0
g = TouchPad(Pin(14))

b_led = Pin(22, Pin.OUT)
b_prev_time = 0
b_interval = 100
b_state = 0
b = TouchPad(Pin(12))


while True:
    r_currentTime = time.ticks_ms()
    if (r.read() < 200 and r_currentTime - r_prev_time > r_interval ):
        r_prev_time = r_currentTime
        if r_state == 1:
            r_state = 0
        else:
            r_state = 1
    r_led.value(r_state)
    r_start_time = time.ticks_ms()
    
    g_currentTime = time.ticks_ms()
    if (g.read() < 200 and g_currentTime - g_prev_time > g_interval ):
        g_prev_time = g_currentTime
        if g_state == 1:
            g_state = 0
        else:
            g_state = 1
    g_led.value(g_state)
    g_start_time = time.ticks_ms()
    
    b_currentTime = time.ticks_ms()
    if (b.read() < 200 and b_currentTime - b_prev_time > b_interval ):
        b_prev_time = b_currentTime
        if b_state == 1:
            b_state = 0
        else:
            b_state = 1
    b_led.value(b_state)
    b_start_time = time.ticks_ms()