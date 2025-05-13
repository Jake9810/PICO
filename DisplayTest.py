from ST7735 import TFT,TFTColor
from sysfont import sysfont
from utime import sleep
from machine import SPI,Pin
# Configurações SPI
spi = SPI(1, baudrate=20000000, polarity=0, phase=0,
          sck=Pin(10), mosi=Pin(11), miso=None)
tft=TFT(spi,16,17,18)
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)
tft.rotation(1)

while True:
    new_line = '\n'
    tft.fill(TFT.WHITE)
    tft.text((1, 40), "Raspberry Pico", TFT.BLACK, sysfont, 2)
    tft.text((1, 60), "Test display", TFT.YELLOW, sysfont, 1.5)
    tft.text((1, 80), "TFT", TFT.BLUE, sysfont, 2)
    sleep(1000)
    tft.fill(TFT.BLACK)
