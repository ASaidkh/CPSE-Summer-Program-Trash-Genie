import RPi.GPIO as GPIO
from time import sleep

#Function to set the angle of vertical servo motor, takes an integer between 0-174 as the degree value
def setVert(angle):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)
	pwm=GPIO.PWM(18, 50)
	pwm.start(0)

	duty = angle / 18 + 3
	GPIO.output(18, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(18, False)
	pwm.ChangeDutyCycle(duty)
	pwm.stop()
	GPIO.cleanup()
#Function to set the angle of the horizontal servo motor, takes an integer between 0-174 as the degree value	
def setHorz(angle):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.OUT)
	pwm=GPIO.PWM(17, 50)
	pwm.start(0)
	
	duty = angle / 18 + 3
	GPIO.output(17, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(17, False)
	pwm.ChangeDutyCycle(duty)
	pwm.stop()
	GPIO.cleanup() 

def center():
    setVert(116)
    setHorz(0)
    
def paper():
    setHorz(15)
    setVert(15)
    center()

def plastic():
    setHorz(85)
    setVert(170)
    center()

def metal():
    setHorz(150)
    setVert(15)
    center()
#Function to move servo motors to dump items into proper compartment, takes a string as an argument
def dump(detection):
    if detection == "METAL":
        metal()
    elif detection == "PLASTIC":
        plastic() 
    elif detection == "PAPER":
        paper()
    


