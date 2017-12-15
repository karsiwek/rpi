import readdist

def readRight():
	return readdist.readDist(16,22)

def readLeft():
	return readdist.readDist(16,18)

def readEyes():
	return [readLeft(), readRight()]	
