import os
import datetime as datetime

a = os.popen("ping www.wp.pl -c1").read()

data = a.split("\n")[1]

now = datetime.datetime.now()
logname = str(now.year)+"-"+str(now.month).zfill(2)+"-"+str(now.day).zfill(2)+".log"

f = open('/logs/networkstat/'+logname, 'a')

data ="\n"+ str(now.hour).zfill(2)+":"+str(now.minute).zfill(2) +" " + data

f.write(data);
