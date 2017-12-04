"""A basic police lights effect."""
import time
from logipy import logi_led

logi_led.logi_led_init()
time.sleep(2)

while True:
    logi_led.logi_led_set_lighting(100, 0, 0)
    time.sleep(0.1)
    logi_led.logi_led_set_lighting(0, 0, 0)
    time.sleep(0.1)
    logi_led.logi_led_set_lighting(100, 0, 0)
    time.sleep(0.1)
    logi_led.logi_led_set_lighting(0, 0, 0)
    time.sleep(0.8)
    logi_led.logi_led_set_lighting(0, 0, 100)
    time.sleep(0.1)
    logi_led.logi_led_set_lighting(0, 0, 0)
    time.sleep(0.1)
    logi_led.logi_led_set_lighting(0, 0, 100)
    time.sleep(0.1)
    logi_led.logi_led_set_lighting(0, 0, 0)
    time.sleep(0.8)
    logi_led.logi_led_set_lighting(100, 100, 100)
    time.sleep(0.1)
    logi_led.logi_led_set_lighting(0, 0, 0)
    time.sleep(0.1)
    logi_led.logi_led_set_lighting(100, 100, 100)
    time.sleep(0.1)
    logi_led.logi_led_set_lighting(0, 0, 0)
    time.sleep(0.8)

logi_led.logi_led_shutdown()
