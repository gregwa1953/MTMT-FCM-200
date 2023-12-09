# ======================================
#  RTC demo with OLED driver.
#  Written by G.D. Walters
# ======================================

from machine import I2C, Pin
from ds1307 import DS1307
#from ssd1306 import SSD1306_I2C
#import framebuf
import time
import utime

# Base setup for the RTC DS1307
rtc_i2c=I2C(0)
rtc=DS1307(rtc_i2c)

# ======================================
# Base setup for the SSD1306
# ======================================
## Set the Width of the OLED Display
#WIDTH = 128
# Set the Height of the OLED Display
#HEIGHT = 32
#oled_i2c = I2C(1)
#oled = SSD1306_I2C(WIDTH, HEIGHT, oled_i2c)
#oled.text("Starting up!", 5,8)
#oled.show()
# ======================================


def ConvertDT(d,which):
    dtin=d
    year=dtin[0]
    month=dtin[1]
    if month < 10:
        monS=f"{month:02d}"
    else:
        monS=str(month)
    day=dtin[2]
    if day<10:
        dayS=f"{day:02d}"
    else:
        dayS=str(month)
    if which==0:
        dow=dtin[3]
        hr=dtin[4]
        if hr < 10:
            hrS=f"{hr:02d}"
        else:
            hrS=str(hr)
        min=dtin[5]
        if min < 10:
            minS=f"{min:02d}"
        else:
            minS=str(min)
        sec=dtin[6]
        if sec < 10:
            secS=f"{sec:02d}"
        else:
            secS=str(sec)
        ss=dtin[7]
    else:
        #dow=dtin[3]
        hr=dtin[3]
        if hr < 10:
            hrS=f"{hr:02d}"
        else:
            hrS=str(hr)
        min=dtin[4]
        if min < 10:
            minS=f"{min:02d}"
        else:
            minS=str(min)
        sec=dtin[5]
        if sec < 10:
            secS=f"{sec:02d}"
        else:
            secS=str(sec)
        ss=dtin[6]        
    # Change the date format to your liking...
    dateS=f"{monS}/{dayS}/{year}"
    timeS=f"{hrS}:{minS}:{secS}"
    return dateS,timeS
# ======================================

    
# ======================================
# Start running
# ======================================

rtc=machine.RTC()
dt=rtc.datetime()
print(f"{dt=}")
d,t=ConvertDT(dt,0)
print(f"RTC: {d} - {t}")
dt=time.localtime()
print(f"{dt=}")
d,t=ConvertDT(dt,1)
print(f"Local Time: {d} - {t}")
loop=True
while loop:
    #oled.fill(0)
    #dt=time.localtime()
    #print(dt)
    d,t=ConvertDT(time.localtime(),1)
    print(f"Local Time: {d} - {t}")
    #time.sleep(1)
    #oled.text(t, 5,8)
    #oled.show()    
    time.sleep(1)
