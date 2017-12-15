import time

notes = {"C": 130.81,\
"D": 146.83,\
"E" : 164.83,\
"F" : 174.61,\
"G" : 196,\
"A" : 220,\
"H" : 246.94, \
"C1" : 261.63}

kanikuly =  {"notes": "CEGFDDEEGGFEFDFDDAAAGGCCAAAGGCEGF",\
"times" : "1111222222111222212222211112222221122222122222"}

alarm = {"notes": "CDHCDHCDHCDHCDHCDHCDHCDH", "times" : "2222222222222222222222"}

timeConst = 0.5
def playNote(device, note, timeToPlay):
	device.ChangeFrequency(notes[note])
	device.start(50)
	time.sleep(timeConst/timeToPlay)
	device.stop()

def playSong(device, song):
	i = 0
	for note in song['notes']:
		playNote(device, note, int(song['times'][i]))
		i=i+1

def playAlarm(device):
	playSong(device, alarm)
