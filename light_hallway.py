from ST7735 import TFT,TFTColor
from sysfont import sysfont
from utime import sleep, ticks_add,ticks_ms,ticks_diff
from machine import SPI,Pin,PWM, ADC

from machine import Pin
import machine
import utime

def promedio(luzP):
    

# Configuraciones SPI primeros pines 10 y 11
spi = SPI(1, baudrate=20000000, polarity=0, phase=0,
          sck=Pin(14), mosi=Pin(15), miso=None)
tft=TFT(spi,16,17,18)
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)
tft.rotation(1)
# configuraciones SPI


led=Pin(25, Pin.OUT)

sensor=machine.ADC(26)

i=0
tft.text((1, 40), "cantidad de luz en la habitacion: ", TFT.PURPLE, sysfont, 1.7)
tft.fillrect((1,75),(80,100),TFT.BLACK)
while(True):
    luz=str(sensor.read_u16())
    #print(sensor.read_u16())
    print(luz)
    utime.sleep(.2)
    tft.fillrect((1,75),(80,100),TFT.BLACK)
    tft.text((1, 80), luz, TFT.PURPLE, sysfont, 2)
    #utime.sleep(.2)

#led.value(0)
    

