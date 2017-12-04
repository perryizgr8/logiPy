"""This cycles fast between random colors and has an RGB intro :P"""
import time
from random import random
from logipy import logi_led

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
    logi_led.logi_led_set_lighting(r, g, b)
    time.sleep(1)
    logi_led.logi_led_set_lighting(100-r, 100-g, 100-b)
    time.sleep(0.5)

logi_led.logi_led_shutdown()
