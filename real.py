from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')
corPlane = []
# the bigger the number is the more accurate the code is gonna be 
tot = [x: 6, y: 6]
# make sure tot and scale factor work toghther
scaleFactor = 1

hub.motion_sensor.reset_yaw_angle()
motion.set_degrees_counted()
# hub.motion_sensor.get_yaw_angle() is how to find 

# start point should be a list: eg [1,3]
def makeMap(startPoint):
    global corPlane, tot
    x = tot.x
    y = tot.y
    # fill out the corPlane
    for xPlace in x:
        corPlane.append([])
        for yPlace in y:
            corPlane[xPlace].append(0)
    #0 is nothing there, 1 is where we are
    corPlane[startPoint[0]][startPoint[1]] =1

def turn(desiredAngle):
    currentAng = hub.motion_sensor.get_yaw_angle()
    change = desiredAngle - currentAng
    return change