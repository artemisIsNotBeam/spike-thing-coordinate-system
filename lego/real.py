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

    #second = abs(startPoint[1]-y)
    second = startPoint[1]
    corPlane[second][startPoint[0]] = 1

def turn(desiredAngle):
    currentAng = hub.motion_sensor.get_yaw_angle()
    change = desiredAngle - currentAng
    return change

def findPosition():
    global corPlane, tot
    x = tot["x"]
    y = tot["y"]
    for xPlace in range(x):
        for yPlace in range(y):
            if corPlane[yPlace][xPlace] == 1:
                return [xPlace,yPlace]

#set in a [x,y]
def calcDist(desiredPos,curPos):
    #time for math(pythagrum theorum)
    #remeber, order dosen't matter cause it will be positive
    xPart = pow(desiredPos[0]-curPos[0],2)
    yPart = pow(desiredPos[1]-curPos[1],2)
    return sqrt(xPart+yPart)
makeMap([1,4])
curPos = findPosition()
dist = calcDist([2,3],[1,4])
print(dist)