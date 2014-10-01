#This exercise is for the use of motors, you should add some delays for you to run your program and see it's 
#functionality. You may use this and modify it for your project.

import RPi.GPIO as io
io.setmode(io.BCM)
import sys, tty, termios, time

# These two blocks of code configure the PWM settings for
# the two DC motors on the RC car. It defines the two GPIO
# pins used for the input, starts the PWM and sets the
# motors' speed to 0

motor1_in1_pin = 4
motor1_in2_pin = 17
io.setup(motor1_in1_pin, io.OUT)
io.setup(motor1_in2_pin, io.OUT)
motor1 = io.PWM(4,100)
motor1.start(0)
motor1.ChangeDutyCycle(0)

motor2_in1_pin = 24
motor2_in2_pin = 25
io.setup(motor2_in1_pin, io.OUT)


io.setup(motor2_in2_pin, io.OUT)
motor2 = io.PWM(4,100)
motor2.start(0)
motor2.ChangeDutyCycle(0)

# This section of code defines the methods used to determine
# whether a motor needs to spin forward or backwards. The
# different directions are acheived by setting one of the
# GPIO pins to true and the other to false. If the status of
# both pins match, the motor will not turn. Check professor's slides!!!

def motor1_forward():
    io.output(motor1_in1_pin, True)
    io.output(motor1_in2_pin, False)

def motor1_reverse():
    io.output(motor1_in1_pin, False)
    io.output(motor1_in2_pin, True)

def motor2_forward():
    io.output(motor2_in1_pin, True)
    io.output(motor2_in2_pin, False)

def motor2_reverse():
    io.output(motor2_in1_pin, False)
    io.output(motor2_in2_pin, True)

#This will tell the motor 2 to go forward with max velocity
    motor2_forward()
    motor2.ChangeDutyCycle(99)
#This will tell the motor 2 to go reverse with max velocity
    motor2_reverse()
    motor2.ChangeDutyCycle(99)
#This will tell the motor2 to stop
    motor2.ChangeDutyCycle(0)

# Program will cease all GPIO activity before terminating
io.cleanup() 
