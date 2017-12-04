"""This tracks cursor position and changes color based on that."""
import time
from random import random
from logipy import logi_led
from ctypes import windll, Structure, c_long, byref

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

pos = queryMousePosition()
#print(pos)

logi_led.logi_led_init()
time.sleep(2)

r = g = b = 0
while True:
    newpos = queryMousePosition()
    if (newpos != pos):
        pos = newpos
        r = int(random() * 100)
        g = int(random() * 100)
        b = int(random() * 100)
        logi_led.logi_led_set_lighting(r, g, b)
    time.sleep(0.1)

logi_led.logi_led_shutdown()
