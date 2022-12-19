#create a function grab temperature and humidity from the DHT12 sensor
def getTempHumid():
    """gets a reading from the DHT12 sensor"""
    #read the sensor
    result = dht12.read()
    #check if we got a good reading
    if result.is_valid():
        #if we got a good reading then return the temperature and humidity
        return result.temperature, result.humidity
    else:
        #if we did not get a good reading then return None for both temperature and humidity
        return None, None

#log temperature and humidity to a file
def logTempHumid(temperature, humidity):
    """logs the temperature and humidity to a file"""
    #open the file
    with open("temp_humidity.txt", "a") as f:
        #write the temperature and humidity to the file
        f.write("{0},{1}")

