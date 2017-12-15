import time
import datetime
import os
from mylibs import rrdlib

inside1 = { "id" : "inside1", "path" : "/sys/bus/w1/devices/28-0000052c3413/w1_slave", "name" : "salon" }
outside1 = { "id" :"outside1", "path" : "/sys/bus/w1/devices/28-0000052c88cb/w1_slave", "name" : "w glebie" }
inside2 = { "id" : "inside2", "path" : "/sys/bus/w1/devices/28-00000613dcfc/w1_slave", "name": "sypialnia"}
outside2 = { "id" : "outside2", "path" : "/sys/bus/w1/devices/28-00000614a6cd/w1_slave", "name" : "parapet"}

therms = [inside1, inside2, outside1, outside2]

values = {}

os.popen("modprobe w1-gpio")
os.popen("modprobe w1-therm")

now = datetime.datetime.now()

for therm in therms :
	tfile = open(therm['path'])
	text = tfile.read()
	tfile.close()
	secondline = text.split("\n")[1]
	temperature = secondline.split(" ")[9]

	temp = float(temperature[2:])/1000.0
	
	values[therm['id']] = temp

	data ="\n"+ str(now.hour).zfill(2)+":"+str(now.minute).zfill(2) +" " + str(temp)
	filename = str(now.year)+"-"+str(now.month).zfill(2)+"-"+str(now.day).zfill(2)+".log"
	wfile = open("/logs/temp/"+therm["id"]+"/"+filename, "a");

	wfile.write(data);
	
	#os.popen('rrdtool graph /logs/temp/'+therm['id']+'/graph.png DEF:'+therm['id']+'=/home/pi/rrd/temp.rdd:'+therm['id']+':AVERAGE LINE2:'+therm['id']+'#FF0000:'+therm['name']+' -s 1404520260');

	#os.popen('rrdtool graph /logs/temp/'+therm['id']+'/''+filename+.png DEF:'+therm['id']+'=/home/pi/rrd/temp.rdd:'+therm['id']+':AVERAGE LINE2:'+therm['id']+'#FF0000:'+therm['name']+' -s 1404520260');

valString = ""
for val in values.values():
	valString=valString+":"+str(val)


timestamp = str(time.mktime(datetime.datetime.now().timetuple()))
os.popen("rrdtool update /home/pi/rrd/temp.rdd "+timestamp+valString)

#print "rrdtool update /home/pi/rrd/temp.rdd "+timestamp+valString;

#os.popen('rrdtool graph /logs/temp/graphs/graph.png --slope-mode -w 700 -h 500 DEF:inside=/home/pi/rrd/temp.rdd:inside1:AVERAGE DEF:outside=/home/pi/rrd/temp.rdd:outside1:AVERAGE  LINE2:inside#FF0000:dom LINE2:outside#00FF00:dwor -s 1404520260');

#os.popen('rrdtool graph /logs/temp/'+filename+'.png DEF:inside=/home/pi/rrd/temp.rdd:inside1:AVERAGE DEF:outside=/home/pi/rrd/temp.rdd:outside1:AVERAGE  LINE2:inside#FF0000:dom LINE2:outside#00FF00:dwor -s 1404520260')

