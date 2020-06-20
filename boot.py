# boot.py -- run on boot-up
from machine import RTC
from network import WLAN
import machine
import time
# RTC
rtc = RTC()
rtc.init()


# connect to wifi
SSID = 'FreeTitties'
passwd = 'wsxw4077'
wlan = WLAN(mode=WLAN.STA, power_save=True)
wlan.connect(SSID, auth=(WLAN.WPA2, passwd))
print("trying to connect to wifi")
while not wlan.isconnected():
    machine.idle()
print("Connected to Wifin")
# get ntp
rtc.ntp_sync('2.fr.pool.ntp.org', update_period=3600)
while not rtc.synced():
    time.sleep_ms(500)
print("ntp sync : " + str(rtc.synced()))
wlan.disconnect()
wlan.deinit()
