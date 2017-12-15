import time
import datetime
import os
from mylibs import rrdlib

inside1 = { "id" : "inside1", "path" : "/sys/bus/w1/devices/28-0000052c3413/w1_slave", "desc" : "w_domu", "col" : "FF0000" }
outside1 = { "id" :"outside1", "path" : "/sys/bus/w1/devices/28-0000052c88cb/w1_slave", "desc" : "na_dworze", "col" : "0000FF" }


inside1 = { "id" : "inside1", "path" : "/sys/bus/w1/devices/28-0000052c3413/w1_slave", "desc" : "salon", "col" : "0000FF" }
outside1 = { "id" :"outside1", "path" : "/sys/bus/w1/devices/28-0000052c88cb/w1_slave", "desc" : "w_glebie", "col" : "00FF00" }
inside2 = { "id" : "inside2", "path" : "/sys/bus/w1/devices/28-00000613dcfc/w1_slave", "desc": "sypialnia", "col" : "FF0000"}
outside2 = { "id" : "outside2", "path" : "/sys/bus/w1/devices/28-00000614a6cd/w1_slave", "desc" : "parapet", "col" : "00FFFF"}


therms = [inside1, inside2, outside1, outside2]

now = datetime.datetime.now()
yesterday = now - datetime.timedelta(1)

rrd = rrdlib.Rrdlib()
rrd.rrdFilename = "/home/pi/rrd/temp.rdd"
rrd.size = [800, 400]
rrd.slope = True
rrd.start = int((yesterday - datetime.datetime(1970, 1,1)).total_seconds())


filename = str(now.year)+"-"+str(now.month).zfill(2)+"-"+str(now.day).zfill(2)+".log"


for therm in therms :
	rrd.graphFile = "/logs/temp/"+therm['id'] + "/graph.png"
	rrd.datas = [therm]

	print rrd.getGraph()
	
	rrd.graphFile = "/logs/temp/"+therm['id'] + "/" + filename+".png"

	print rrd.getGraph()

rrd.graphFile = "/logs/temp/graphs/graph.png"
rrd.datas = therms;

print rrd.getGraph()

rrd.graphFile = "/logs/temp/graphs/" + filename + ".png"
print rrd.getGraph()
