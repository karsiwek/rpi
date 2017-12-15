import time
import RPi.GPIO as GPIO
import readdist

dioden = [22, 18, 16, 12,10]
button = 15
distInput = 13
distTrigger = 11

def setup():
	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD)
	for port in dioden:
		GPIO.setup(port, GPIO.OUT)
	GPIO.setup(button, GPIO.OUT)

normaliser = 10;


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
print "start"
while 1:
	dist = readdist.readDist( distTrigger, distInput)
	print dist
	leds = min(len(dioden),int(dist/normaliser))
	print leds
	setup()
	for port in dioden:
		GPIO.output(port,0)

	for port in dioden[0:leds]:
		GPIO.output(port,1)
	time.sleep(0.1)

GPIO.cleanup()

