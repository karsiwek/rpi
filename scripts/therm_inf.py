import time

while True:

	tfile = open("/sys/bus/w1/devices/28-0000052c3413/w1_slave")

	text = tfile.read()

	tfile.close()

	secondline = text.split("\n")[1]

	temperature = secondline.split(" ")[9]

	temp = float(temperature[2:])/1000.0

	print temp



