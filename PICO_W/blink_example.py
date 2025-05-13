import machine

from utime import sleep

led=machine.Pin("LED", machine.Pin.OUT)
opc=False

while True:
    opc=not opc
    led.on()
    print(opc)
    sleep(1)
    led.off()
    sleep(1)

