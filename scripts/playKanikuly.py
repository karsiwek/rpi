import RPi.GPIO as GPIO
import notes

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

notes.playAlarm(p)
notes.playSong(p, notes.kanikuly)
