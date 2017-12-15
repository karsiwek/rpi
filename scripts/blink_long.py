import time
import RPi.GPIO as GPIO

PORT = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PORT, GPIO.OUT)

for i in range(3):
	GPIO.output(PORT, 1)
	time.sleep(1)
	GPIO.output(PORT, 0)
	time.sleep(1)
GPIO.cleanup()

