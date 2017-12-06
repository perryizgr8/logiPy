"""This tracks CPU usage and changes color based on that."""
import time
import subprocess
from logipy import logi_led
logi_led.logi_led_init()
time.sleep(2)

def getcpu():
    p = subprocess.Popen('wmic cpu get loadpercentage', shell=True, stderr=None, stdout=subprocess.PIPE)
    op = p.communicate()
    return int(str(op[0]).split(" ")[2].split("n")[1])

def getclass(load):
    if load < 33:
        return 'green'
    elif load < 67:
        return 'yellow'
    else:
        return 'red'

def setcolor(loadclass):
    if loadclass == 'green':
        logi_led.logi_led_set_lighting(0, 100, 0)
    elif loadclass == 'yellow':
        logi_led.logi_led_set_lighting(100, 100, 0)
    elif loadclass == 'red':
        logi_led.logi_led_set_lighting(100, 0, 0)

logi_led.logi_led_set_lighting(0, 0, 0)
loadclass = 'green'
while True:
    load = getcpu()
    newloadclass = getclass(load)
    if(newloadclass != loadclass):
        loadclass = newloadclass
        setcolor(loadclass)
    time.sleep(0.1)

logi_led.logi_led_shutdown()
