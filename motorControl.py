#This code will make your motor move for two seconds
#hovercraft should use this code for turning on their motors.

import RPi.GPIO as GPIO # access RPi.GPIO module
from time import sleep
 
GPIO.setmode(GPIO.BOARD)#The function setmode tells RPi.GPIO to use the board numbering on the Raspberry Pi. 
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
print "Turning motor on"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(2)
 
print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
 
GPIO.cleanup()
