import time
import RPi.GPIO as GPIO
prec = 5
def readDist(trigger, input):

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(trigger, GPIO.OUT)
	GPIO.setup(input, GPIO.IN)


	startTime = time.time()
	GPIO.output(trigger,0)
	probes = []
	while len(probes)<prec:
		testStartTime = time.time()
		startTime = testStartTime
		GPIO.output(trigger, 1)
		time.sleep(0.00001)
		GPIO.output(trigger, 0)

		while GPIO.input(input) != 1 and startTime-testStartTime<1:
			startTime = time.time()
		while GPIO.input(input) != 0:
			pass		
		now = time.time()
		if startTime-testStartTime > 1:
			pass	
		probes.append(34000.0*(now-startTime)/2)
	probes.sort()
	GPIO.cleanup()
	if prec > 3:
		return sum(probes[1:(prec-1)])/3
	elif prec ==1 :
		return probes[0]
	else :
		return sum(probes)/len(probes)

