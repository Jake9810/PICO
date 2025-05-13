##programa para controlar un servo sg90 con un potenciometro

from machine import Pin, PWM, ADC
from utime import sleep

servo=PWM(Pin(0))
pot=ADC(28)
servo.freq(50)

in_min=0
in_max=65535

out_min=1000
out_max=9000

while True:
    val=pot.read_u16()
    
    srv=(val-in_min)*(out_max-out_min)/(in_max - in_min)+out_min
    
    servo.duty_u16(int(srv))

