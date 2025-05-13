from machine import Pin
import utime

led=Pin(25,Pin.OUT)
boton=Pin(15,Pin.IN,Pin.PULL_DOWN)
opc=0

while True:
    if(boton.value()==1):
        led.value(1)
        print(boton.value())
        opc=1
        utime.sleep(1)
        while opc==1:
            led.value(1)
            print(opc)
            if(boton.value()==1):
                opc=0
            else:
                opc=1
            utime.sleep(1)
    else:
        led.value(0)
        print(boton.value())
        utime.sleep(1)
