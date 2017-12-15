import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

for i in range(10):
	GPIO.output(12, not GPIO.input(12))
	time.sleep(0.1)
	GPIO.output(12, not GPIO.input(12))
	time.sleep(0.1)
GPIO.cleanup()

