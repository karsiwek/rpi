import time
import RPi.GPIO as GPIO

dioden = [22, 18, 16, 12,10, 11, 13]
button = 15

GPIO.setmode(GPIO.BOARD)

for port in dioden :
	GPIO.setup(port, GPIO.OUT)

GPIO.setup(button, GPIO.OUT)


multipler = 1
def pressedAction():
	global multipler
	multipler = multipler*(-1)

status = 0
def pressed(input) :
	global status 
	if input != status:
		if input == 1:
			status = 1
			pressedAction()
		status = input

actLED = -1
for port in dioden:
	GPIO.output(port, 0)
for i in range(200):
	actLED = (actLED + multipler)%len(dioden)
	print actLED;
	actPort = dioden[actLED]
	pressed(GPIO.input(button))
	GPIO.output(actPort, 1)
	time.sleep(0.1)
	GPIO.output(actPort, not GPIO.input(actPort))

GPIO.cleanup()

