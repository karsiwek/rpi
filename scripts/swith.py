import time
import RPi.GPIO as GPIO

PORT = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PORT, GPIO.OUT)

GPIO.output(PORT, 1)
time.sleep(2)
GPIO.output(PORT, 0)

GPIO.cleanup()

