import RPi.GPIO as GPIO
import dht11
import time
import datetime
from beebotte import *

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
bbt = BBT("42430858454ce529fc32d3c39a5ac5a8", "1fe805ea9333b67797aac6acefea184456ad5e9bed6256e5b4a0a1275564ed06")

temp_resource   = Resource(bbt, 'jeze', 'temperatura')
humid_resource  = Resource(bbt, 'jeze', 'wilgotnosc')

# read data using pin 14
instance = dht11.DHT11(pin=14)
valid = False
while not valid:
    result = instance.read()
    valid = result.is_valid()
    if valid:
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
	temp_resource.write(result.temperature)
	humid_resource.write(result.humidity)

#    time.sleep(1)
