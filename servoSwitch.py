from ST7735 import TFT,TFTColor
from sysfont import sysfont
from utime import sleep, ticks_add,ticks_ms,ticks_diff
from machine import SPI,Pin,PWM, ADC

def contador(s,m1,h1):
    if(s>=59):
        m1+=1
        s=0
    if(m1>=59):
        h1+=1
        m1=0
        s=0
    return s,m1,h1

# Configuraciones SPI primeros pines 10 y 11
spi = SPI(1, baudrate=20000000, polarity=0, phase=0,
          sck=Pin(14), mosi=Pin(15), miso=None)
tft=TFT(spi,16,17,18)
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)
tft.rotation(1)

servo=PWM(Pin(0))
led=Pin(25,Pin.OUT)
sw=Pin(13,Pin.IN,Pin.PULL_DOWN)
#pot=ADC(28)
servo.freq(50)

Min=1000000

Max=2000000
x=0
m=0
h=0
#opc=0
servo.duty_ns(Min)

while True:
    x,m,h=contador(x,m,h)
    tft.text((1, 40), "Timepo activo: ", TFT.PURPLE, sysfont, 2)
    tft.fillrect((1,60),(80,100),TFT.BLACK)
    #tft.text((1, 80), str(h)+":"+str(m)+":"+str(x), TFT.PURPLE, sysfont, 2)
    #sleep(1)
    #x=x+1
    tft.text((1, 60), str(h)+":"+str(m)+":"+str(x), TFT.PURPLE, sysfont, 2)
    x=x+1
    sleep(1)
    if(sw.value()==1):
        led.value(1)
        #print(sw.value())
        opc=1
        led.value(1)
        #print(opc)
        servo.duty_ns(Min)
        sleep(2)
        servo.duty_ns(Max)
        sleep(1)
        #tft.fillrect((1,80),(80,100),TFT.BLACK)
        tft.fillrect((1,60),(80,100),TFT.BLACK)
        x=x+3
        tft.text((1, 60), str(h)+":"+str(m)+":"+str(x), TFT.PURPLE, sysfont, 2)   
    else:
        #opc=0
        #print(opc)
        led.value(0)
        servo.duty_ns(Min)
       
