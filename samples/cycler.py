from logipy import logi_led
import time
from random import *

logi_led.logi_led_init()
time.sleep(1)

r = g = b = 0
logi_led.logi_led_set_lighting(r, g, b)
time.sleep(5)

def transition(r, g, b, new_r, new_g, new_b):
    while ((r != new_r) or (g != new_g) or (b != new_b)):
        while (r != new_r):
            if (r > new_r):
                r = r - 1
                break
            else:
                r = r + 1
                break
            #logi_led.logi_led_set_lighting(r, g, b)
            #time.sleep(0.01)
    
        while (g != new_g):
            if (g > new_g):
                g = g - 1
                break
            else:
                g = g + 1
                break
            #logi_led.logi_led_set_lighting(r, g, b)
            #time.sleep(0.01)
        
        while (b != new_b):
            if (b > new_b):
                b = b - 1
                break
            else:
                b = b + 1
                break
            #logi_led.logi_led_set_lighting(r, g, b)
            #time.sleep(0.01)
        logi_led.logi_led_set_lighting(r, g, b)
        time.sleep(0.01)

yolo = 0
while True:
    new_r = int(random() * 100)
    new_g = int(random() * 100)
    new_b = int(random() * 100)
    transition(r, g, b, new_r, new_g, new_b)
    r = new_r
    g = new_g
    b = new_b
    time.sleep(3)
    logi_led.logi_led_set_lighting(100 - r, 100 - g, 100 -b)
    time.sleep(0.1)
#    if(yolo == 0):
#        logi_led.logi_led_set_lighting(100, 0, 0)
#        yolo = 1
#    elif(yolo == 1):
#        logi_led.logi_led_set_lighting(0, 100, 0)
#        yolo = 2
#    else:
#        logi_led.logi_led_set_lighting(0, 0, 100)
#        yolo = 0
#    time.sleep(0.5)
#    logi_led.logi_led_set_lighting(r, g, b)

#time.sleep(10)

logi_led.logi_led_shutdown()