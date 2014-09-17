from Tkinter import * #this allows you to use GUI
import RPi.GPIO as GPIO #import library for controlling the servo by software
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) # port where you are supouse to connect you servo motor!
pwm = GPIO.PWM(18, 100)
pwm.start(5)

class App:

    def __init__(self, master): #initializates the Graphical User Interface
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180,
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(duty) #Modifies the wave duty cycle for you to have different possitions in your servo motor.

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()
# this would hel you change your  angle in the hovercraft project, but maybe you should modify the code a bit
# because you do not need a GUI I gues...
