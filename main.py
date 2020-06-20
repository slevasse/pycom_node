# main.py -- put your code here!
from pysense import Pysense
from LIS2HH12 import LIS2HH12
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2
from SI7006A20 import SI7006A20
import time
import machine
from network import WLAN
from machine import RTC

# declare the pysense object
wipy = Pysense()
# declare the light sensor
lightSense = LTR329ALS01(pysense=wipy)
#pressureSense = MPL3115A2(pysense=wipy, mode=0)  # alti mode
pressureSense = MPL3115A2(pysense=wipy, mode=1)  #  pressure mode
humidTempSense = SI7006A20(pysense=wipy)

# RTC
rtc = RTC()
#rtc.init()


while True:
    lux = lightSense.light()
    temp = humidTempSense.temperature()
    humid = humidTempSense.humidity()
    pressure = pressureSense.pressure()
    #alti = pressureSense.altitude()
    temp2 = pressureSense.temperature()
    print("time: " + str(rtc.now()))
    print("lux : " + str(lux[0]))
    print("temp1 : " + str(temp))
    print("temp2 : " + str(temp2))
    print("humid : " + str(humid))
    print("pressure : " + str(pressure))
    print("")
    #print("alti : " + str(alti))
    #machine.deepsleep(50000)
    machine.sleep(10000)
    #machine.idle()
    #time.sleep_ms(5000)
