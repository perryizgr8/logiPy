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
    logi_led.logi_led_flash_lighting(100, 0, 0, 500, 500)

logi_led.logi_led_shutdown()