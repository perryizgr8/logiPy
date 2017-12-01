from logipy import logi_led
import time
from random import *

logi_led.logi_led_init()
time.sleep(2)

r = g = b = 0
logi_led.logi_led_set_lighting(100, 0, 0)
time.sleep(5/3)
logi_led.logi_led_set_lighting(0, 100, 0)
time.sleep(5/3)
logi_led.logi_led_set_lighting(0, 0, 100)
time.sleep(5/3)

yolo = 0
while True:
    r = int(random() * 100)
    g = int(random() * 100)
    b = int(random() * 100)
    #time.sleep(3)
    logi_led.logi_led_set_lighting(r, g, b)
    time.sleep(0.2)
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