import sys
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO more info
import time
from collections import namedtuple

# try: 
#     direction = sys.argv[1]
#     steps = int(float(sys.argv[2]))
#     mnum = sys.argv[3]
# except:
#     steps = 0
 
def turnMotor(direction, steps, mnum):
    #print which direction and how many steps 
    if steps == 0:
        return;

    print("You told me to turn %s %s steps.") % (direction, steps)

    #Step 3: Setup the raspberry pi's GPIOs
    #------------------------------------------------------------------------
    #------------------------------------------------------------------------
    #use the broadcom layout for the gpio
    gpio.setmode(gpio.BCM)
    #Motor 1
    #GPIO23 = Direction
    #GPIO24 = Step
    #-------------------
    #Motor 2
    #GPIO17 = Direction
    #GPIO27 = Step
    #-------------------
    #Motor 3
    #GPIO22 = Direction
    #GPIO25 = Step
    #-------------------
    #Motor 4
    #GPIO5 = Direction
    #GPIO6 = Step
    #-------------------
    #Motor 5
    #GPIO26 = Direction
    #GPIO16 = Step
    Motor = namedtuple("Motor", "dirPin stepPin")
    MotorList = []
    MotorList.append(Motor(23, 24))
    MotorList.append(Motor(17, 27))
    MotorList.append(Motor(22, 25))
    MotorList.append(Motor(5, 6))
    MotorList.append(Motor(26, 16))

    #print(MotorList)
    #print(MotorList[1].stepPin)
    #print(MotorList[mnum].stepPin)

    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(17, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(25, gpio.OUT)
    gpio.setup(5, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.setup(26, gpio.OUT)
    gpio.setup(16, gpio.OUT)
    #------------------------------------------------------------------------
    #------------------------------------------------------------------------
     
     
    #Step 4: Set direction of rotation
    #------------------------------------------------------------------------
    #------------------------------------------------------------------------
    #set the output to true for left and false for right
    if direction == 'left':
        gpio.output(MotorList[mnum].dirPin, True)
    elif direction == 'right':
        gpio.output(MotorList[mnum].dirPin, False)
    #------------------------------------------------------------------------
    #------------------------------------------------------------------------
     
     
    #Step 5: Setup step counter and speed control variables
    #------------------------------------------------------------------------
    #------------------------------------------------------------------------
    #track the number of steps taken
    StepCounter = 0
     
    #waittime controls speed
    WaitTime = 0.01
    #------------------------------------------------------------------------
    #------------------------------------------------------------------------
     
     
    #Step 6: Let the magic happen
    #------------------------------------------------------------------------
    #------------------------------------------------------------------------
    # Start main loop
    while StepCounter < steps:
     
        #turning the gpio on and off tells the easy driver to take one step
        gpio.output(MotorList[mnum].stepPin, True)
        gpio.output(MotorList[mnum].stepPin, False)
        StepCounter += 1
     
        #Wait before taking the next step...this controls rotation speed
        time.sleep(WaitTime)
    #------------------------------------------------------------------------
    #------------------------------------------------------------------------
     
     
    #Step 7: Clear the GPIOs so that some other program might enjoy them
    #------------------------------------------------------------------------
    #------------------------------------------------------------------------
    #relase the GPIO
    gpio.cleanup()
    #------------------------------------------------------------------------
    #------------------------------------------------------------------------