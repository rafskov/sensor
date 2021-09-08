

from sds011 import *
import time 
from aqi import *


sensor = SDS011("/dev/ttyUSB0")

#get 3 datums to average
def get_data(n=3):
    pm2 = 0
    pm10 = 0
    time.sleep(10)
    for i in range(n):
        pm2 = pm2 + x[0]
        pm10 = pm10 + x[1]
        time.sleep(2)
    pm2 = round(pm2/n,1)
    pm10 = round(pm10/n,1)


def conv_aqi(pm2,pm10):
    aqi2 = aqi.to.iaqi(aqi.POLLUTANT_PM25,str(pm2))
    aqi10 = aqi.to.iaqi(aqi.POLLUTANT_PM10,str(pm10))
    return aqi2,aqi10

pm2,pm10 = get_data()
aqi2,aqi10 = conv_aqi(pm2,pm10)
print( f" pm2.5  = {aqi} ug/m3 (AQI: {aqi2})",end="")
print( f" pm10  = {aqi} ug/m3 (AQI: {aqi10})",end="")





