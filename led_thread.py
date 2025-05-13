import machine
import _thread
from utime import sleep

led=machine.Pin(15, machine.Pin.OUT)
boton=machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
opc=False

global botonP
botonP=False

def readerButtonthread():
    global botonP
    while True:
        if boton.value() == 1:
            botonP = True
        sleep(0.01)
_thread.start_new_thread(readerButtonthread, ())

while True:
    if(botonP == True):
        opc=not opc
        led.value(opc)
        sleep(0.01)
        botonP=False

