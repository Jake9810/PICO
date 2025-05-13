import machine
import utime

led=machine.Pin(15,machine.Pin.OUT)
boton=machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)

def latching(b):
    if(b.value()==1):
        return True
    else:
        return False
opc=False
while True:
    #opc=latching(boton)
    if(boton.value()==1):
        opc=not opc
        led.value(opc)#print(opc)
        utime.sleep(0.01)
    else:
        pass
        #print(opc)
        #utime.sleep(0.99)
    
    
'''
#opc=boton.value()
    if boton.value()==1:
        led.value(1)
        opc=1
        while opc==1:
            led.value(1)#opc=1
            if(boton.value()==1):
                led.value(0)
                opc=0
                break
    else:
        led.value(0)
'''