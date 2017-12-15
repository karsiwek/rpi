import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

times = []
change = False
val = GPIO.input(16);
startTime = time.time()
offsetTime = time.time()
lastChange = time.time()

end = False;
while not end:
	now = time.time()
	if val != GPIO.input(16):
		times.append(now - startTime)	
		lastChange = now;
		val = not val;
		print("change");
	if now - lastChange > 3:
		end = True
	time.sleep(0.01)
print(times)



GPIO.setup(12, GPIO.OUT)
GPIO.output(12, 0)

startTime = time.time()
end = False
index = 0
while not end:
	now = time.time()
	if times[index] < now - startTime:
		GPIO.output(12,0)
		time.sleep(0.1)
		GPIO.output(12,1)
		index = index+1
		if index >= len(times):
			end = True
	else:
		time.sleep(0.01)

GPIO.cleanup()
