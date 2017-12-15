import time
import RPi.GPIO as GPIO

def move(angle):
	start = 2.5
	end = 12.5

	freq = ((angle+90.0)/180.0)*(12.5-2.5) + 2.5
	print(freq)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(15, GPIO.OUT)

	pwm = GPIO.PWM(15, 50)

	pwm.start(freq)

	time.sleep(1)
	pwm.stop()
#	GPIO.cleanup()


