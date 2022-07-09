from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

import sys
hub = PrimeHub()


lightSensor = PrimeHub.PORT_D
arm = PrimeHub.PORT_F
leftMotor = Motor("C")
rightMotor = Motor("B")
motorPair = MotorPair('C','B')

hub.light_matrix.show_image('HAPPY')
corPlane = []
tot = {"x": 6, "y": 6}
# make sure tot and scale factor work toghther
scaleFactor = 18
unit = "in"

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

# find angle with 
def findTurnturn(desiredAngle):
    currentAng = hub.motion_sensor.get_yaw_angle()
    change = desiredAngle - currentAng
    return change

#for loops to find position
def findPosition():
    global corPlane, tot
    x = tot["x"]
    y = tot["y"]
    for xPlace in range(x):
        for yPlace in range(y):
            if corPlane[yPlace][xPlace] == 1:
                return [xPlace,yPlace]

# this sets the new 1 to pos and rest to zero
def update(pos):
    global corPlane, tot
    x = tot["x"]
    y = tot["y"]
    for xPlace in range(x):
        for yPlace in range(y):
            if (xPlace ==pos[0] and yPlace==pos[1]):
                corPlane[yPlace][xPlace] = 1
            else:
                corPlane[yPlace][xPlace] = 0

def calcDist(desiredPos,curPos):
    # distance formula math :(
    xPart = pow(desiredPos[0]-curPos[0],2)
    yPart = pow(desiredPos[1]-curPos[1],2)
    return sqrt(xPart+yPart)

def move(desiredPos):
    # so basically you 
    global motorPair, unit
    curPos = findPosition()
    dist = calcDist(desiredPos,curPos)
    ang = findAng(desiredPos,curPos)
    ang = findTurnturn(ang)
    # find the angle with complex yaw calculations
    # motorPair.move()

    print("angle "+str(ang))
    print("dist "+str(dist))
    
    turn(ang)
    #NOTE: YOU CAN'T TURN 180 degerees with with turn, just break up 
    # the turn with smaller turns
    motorPair.move(dist,unit=unit,steering=0, speed=50)
    """
    negative is left, pos is to the right

    steering has nothing to do with the angle

    instead we should use a turn of both motors and then 
    """
    update(desiredPos)


#set in a [x,y]
def calcDist(desiredPos,curPos):
    #time for math(pythagrum theorum)
    #remeber, order dosen't matter cause it will be positive
    xPart = pow(desiredPos[0]-curPos[0],2)
    yPart = pow(desiredPos[1]-curPos[1],2)
    return sqrt(xPart+yPart)

def findAng(desiredPos,curPos):
    xPart = (desiredPos[0]-curPos[0]) * scaleFactor
    yPart = (desiredPos[1]-curPos[1]) * scaleFactor

    print("x "+str(xPart)+"y " +str(yPart))
    #x would be adjacent, y would be opposite
    return degrees(atan(yPart/xPart))

def turn(Ang):
    # need rounded because dosen't return fakes
    global hub,leftMotor,rightMotor
    desiredModAng = hub.motion_sensor.get_yaw_angle() + Ang
    desiredModAng = round(desiredModAng)
    print(desiredModAng)

    leftMotor.start_at_power(30)
    rightMotor.start_at_power(30)

    shouldGo = True
    while shouldGo == True:
        curAng = hub.motion_sensor.get_yaw_angle()
        if curAng == desiredModAng:
            print("im done ayayayyayayay")
            break
    leftMotor.stop()
    rightMotor.stop()


#BIG NOTE: don't make yourself do a 180 it will freeze/ break the robot
makeMap([1,0])
print(corPlane)