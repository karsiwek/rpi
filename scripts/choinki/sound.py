import time
import RPi.GPIO as GPIO

port = 22
button = 15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(port, GPIO.OUT)

GPIO.setup(button, GPIO.OUT)


GPIO.output(port, 0)
for i in range(1000):
	GPIO.output(port, 1)
	time.sleep(0.0001)
	GPIO.output(port, 0)
	time.sleep(0.0002)

GPIO.cleanup()

