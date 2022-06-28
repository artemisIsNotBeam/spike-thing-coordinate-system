from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')
corPlane = []
tot = {"x": 6, "y": 6}
# make sure tot and scale factor work toghther
scaleFactor = 1


lightSensor = PrimeHub.PORT_D
arm = PrimeHub.PORT_F
leftMotor = PrimeHub.PORT_B
rightMotor = PrimeHub.PORT_C
motorPair = MotorPair('B','C')

hub.motion_sensor.reset_yaw_angle()
# hub.motion_sensor.get_yaw_angle() is how to find 



# start point should be a list: eg [1,3]
# warning, this function will have 
def makeMap(startPoint):
    global corPlane, tot
    x = tot["x"]
    y = tot["y"]
    # fill out the corPlane
    for xPlace in range(x):
        corPlane.append([])
        for yPlace in range(y):
            corPlane[xPlace].append(0)
    #0 is nothing there, 1 is where we are

    second = abs(startPoint[1]-y)
    corPlane[second][startPoint[0]] = 1

def turn(desiredAngle):
    currentAng = hub.motion_sensor.get_yaw_angle()
    change = desiredAngle - currentAng
    return change

