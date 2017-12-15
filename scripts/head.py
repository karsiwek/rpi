import readEyes
import time
import moveservo
import threading

angle = 0
prec = 20

def move(ang):	
	threading.Thread(target=moveservo.move, args=[angle]).start()

while True:
	eyes = readEyes.readEyes()
	print eyes
	if eyes[0] < 100 or eyes[1] < 100:
	
		if eyes[0] - eyes[1] > prec:
			print("move left")
			angle = angle +10
			move(angle)
			time.sleep(0.5)
		elif eyes[1] - eyes[0] > prec:
			print("move right")
			angle = angle -10
			move(angle)
			time.sleep(0.5)
		else:
			print("no changes");
	else:
		print("don't see")
#	move(angle)
	time.sleep(0.1)
