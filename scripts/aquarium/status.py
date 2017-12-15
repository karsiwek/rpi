import time
import RPi.GPIO as GPIO
import sys
import datetime

OFF = GPIO.OUT
ON = GPIO.IN

PORT_LIGHT = 12
PORT_FILTER = 16
PORT_HEATER = 18

defaults = {PORT_LIGHT : ON,
	PORT_FILTER : ON,
	PORT_HEATER : ON}

GPIO.setmode(GPIO.BOARD)

PORT = -1

if sys.argv[1] == "auto":

	hour = datetime.datetime.now().time().hour	
	
	if hour >=22 or hour <7 :
		defaults[PORT_LIGHT] = OFF

	for key in defaults.keys():
		GPIO.setup(key, defaults[key])
elif sys.argv[1] == "light":
	PORT = PORT_LIGHT
elif sys.argv[1] == "filter":
	PORT = PORT_FILTER
elif sys.argv[1] == "heater":
	PORT = PORT_HEATER

if sys.argv[1] != "auto":
	if sys.argv[2] == "off":
		GPIO.setup(PORT, GPIO.OUT)
	else:
		GPIO.setup(PORT, GPIO.IN)


