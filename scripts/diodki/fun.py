import numpy
import os;
import time;
import random
import math
import colorsys

os.popen("./diodki_lib 1 1 1 1 1 1 1 0").read()

oldVals = [0,0,0,0,0,0,0,0]
oldValsPointer = 0;

hsvPointer = 0;

for i in range(255):
	oldValsPointer = (oldValsPointer+1)%8;
	color = colorsys.hsv_to_rgb(1.0*hsvPointer/360,1,0.8);
	hsvPointer = (hsvPointer+10)%360
	
	rgbCol = [int(color[0]*100), int(color[1]*100), int(color[2]*100)]
	print rgbCol
	if int(i/8)%2 == 1:
		oldVals = numpy.roll(oldVals,1)
	else:
		oldVals = numpy.roll(oldVals,7)

	oldVals[0] = rgbCol[0]*0x10000 + rgbCol[1]*0x100 + rgbCol[2];
	cmd = "./diodki_lib "+" "+" ".join(map(str, oldVals))
	print cmd
	os.popen(cmd).read()
	#time.sleep(0.01);
