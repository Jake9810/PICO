import machine
import utime
analog_value = machine.ADC(28)
#potenciometro de 250k
#resistencia de 30839
file=open("data_campo.txt","w")
date=utime.localtime()
d=str(date[2])+"/"+str(date[1])+"/"+str(date[0])
file.write(d+"\n")
while True:
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    file.write(str(reading)+"\n")
    utime.sleep(0.2)
file.flush()
'''
import machine
import utime
analog_value = machine.ADC(28)
#potenciometro de 250k
#resistencia de 30839
file=open("data_campo.txt","w")
date=utime.localtime()
#d=str(date[2])+"/"+str(date[1])+"/"+str(date[0])
#file.write("date recorded: ","\n")
while True:
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    file.write("ADC: ",str(reading),"\n")
    utime.sleep(0.2)
file.write("--------------\n")
file.flush()
'''
