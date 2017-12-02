"""Random colors with smooth transition and a pulse before every change."""
import time
from random import random
from logipy import logi_led

logi_led.logi_led_init()
time.sleep(1)

r = g = b = 0
logi_led.logi_led_set_lighting(r, g, b)
time.sleep(5)

def transition(red, green, blue, new_red, new_green, new_blue):
    """This smoothly transitions from one color to another."""
    while (red != new_red) or (green != new_green) or (blue != new_blue):
        while red != new_red:
            if red > new_red:
                red = red - 1
                break
            else:
                red = red + 1
                break
        while green != new_green:
            if green > new_green:
                green = green - 1
                break
            else:
                green = green + 1
                break
        while blue != new_blue:
            if blue > new_blue:
                blue = blue - 1
                break
            else:
                blue = blue + 1
                break
        logi_led.logi_led_set_lighting(red, green, blue)
        time.sleep(0.01)

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

logi_led.logi_led_shutdown()
