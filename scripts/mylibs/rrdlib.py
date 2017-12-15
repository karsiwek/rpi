import os

class Rrdlib():

	datas = []
	desc = ""
	rrdFilename = ""
	graphFile = ""
	start = ""		
	size = ""
	slope = False

#1404520260

	def getGraph(self):
		command = 'rrdtool graph ' + \
self.graphFile + ' '

		if self.size != "" :
			command = command + "-w " + str(self.size[0]) + " -h " + str(self.size[1]) + " "
		if self.slope == True :
			command = command + "--slope-mode "
		
		for data in self.datas:
			command = command + \
'DEF:'+data['id']+'='+self.rrdFilename+':'+data['id']+':AVERAGE '+ \
'LINE2:'+data['id']+'#'+data['col']+':'+data['desc']+' '

		if self.start != "" :
			command = command + "-s " + str(self.start) +" "
			
		
		os.popen(command)
		return command;
