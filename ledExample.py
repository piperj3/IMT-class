import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
# number 18 refers to the port where you are supouse to connect your LED, but if needed you can change it.
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, True) #LED ON
GPIO.output(18, False) #LED OFF
