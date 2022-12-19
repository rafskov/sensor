
#use ADAFRUIT DHT12 sensor
import adafruit_dht

#create function using ADAFRUIT DHT12 to get temperature and humidity
def get_temp_humid():
    dhtDevice = adafruit_dht.DHT12(board.D4)
    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity
    return temperature, humidity

#create function to log temperature and humidity to file
def log_temp_humid():
    temperature, humidity = get_temp_humid()
    with open("sensor2.txt", "a") as f:
        f.write("{},{}".format(temperature, humidity))




