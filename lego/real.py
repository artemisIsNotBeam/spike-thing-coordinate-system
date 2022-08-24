from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *


hub = PrimeHub()


lightSensor = PrimeHub.PORT_D
arm = PrimeHub.PORT_F
leftMotor = Motor("B")
rightMotor = Motor("C")
motorPair = MotorPair('C','B')

hub.light_matrix.show_image('HAPPY')
corPlane = []


# Height is 39 inches and 80 inches wide
tot = {"x": 40, "y": 20}

unit = "in"
hub.motion_sensor.reset_yaw_angle()



# start point should be a list: eg [1,3]
# warning, this function will have 
def makeMap(startPoint):
    global corPlane, tot
    x = tot["x"]
    y = tot["y"]
    # fill out the corPlane
    for yPlace in range(y):
        tempList = []
        for xPlace in range(x):
            tempList.append(0)
        corPlane.append(tempList)
        
    #0 is nothing there, 1 is where we are

    #second = abs(startPoint[1]-y)
    second = startPoint[1] -1
    first = startPoint[0] - 1
    corPlane[second][first] = 1

# find angle with 
def findTurnturn(desiredAngle):
    currentAng = hub.motion_sensor.get_yaw_angle()
    change = currentAng - desiredAngle
    return change

#for loops to find position
def findPosition():
    global corPlane, tot
    x = tot["x"]
    y = tot["y"]

    for yPlace in range(y):
        for xPlace in range(x):
            if corPlane[yPlace][xPlace] == 1:
                return [xPlace,yPlace]
                print("I found it")
    

# this sets the new 1 to pos and rest to zero
def update(pos):
    global corPlane, tot
    x = tot["x"]
    y = tot["y"]

    tempList = []

    curPos = findPosition()
    for xPlace in range(x):
        for yPlace in range(y):
            if curPos[0] == xPlace and curPos[1] == yPlace:
                corPlane[xPlace][yPlace] = 0
                
    for newx in range(x):
        if pos[0] == newx:
            tempList.append(1)
        else:
            tempList.append(0)
    corPlane[pos[1]] = tempList


def calcDist(desiredPos,curPos):
    # distance formula math :(
    xPart = pow(desiredPos[0]-curPos[0],2)
    yPart = pow(desiredPos[1]-curPos[1],2)
    return sqrt(xPart+yPart)

def move(desiredPos, quad):
    # so basically you 
    global motorPair, unit
    curPos = findPosition()
    dist = calcDist(desiredPos,curPos)
    ang = findAng(desiredPos,curPos, quad)
    #ang = findTurnturn(ang)
    # find the angle with complex yaw calculations
    # motorPair.move()
    turn(ang)
    #NOTE: YOU CAN'T TURN 180 degerees with with turn, it will just break up 
    # the turn with smaller turns
    print("distance"+ str(dist))
    motorPair.move( (-1 * dist),unit=unit,steering=0, speed=50)
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

    print(desiredPos, curPos)
    xPart = pow(desiredPos[0]-curPos[0],2) 
    yPart = pow(desiredPos[1]-curPos[1],2) 
    return sqrt(xPart+yPart)

def findAng(desiredPos,curPos,quad):
    xPart = (desiredPos[0]-curPos[0]) 
    yPart = (desiredPos[1]-curPos[1]) 


    print(curPos)
    if xPart == 0:
        print("zero angle smh")
        return 0

    if yPart == 0:
        print("its zero")
        return 0
    noApply = degrees(atan(xPart / yPart))

    if quad == 2:
        noApply += 90
    if quad == 3:
        noApply *= -1
        noApply -= 90
    if quad == 4:
        noApply *= -1
    #x would be adjacent, y would be opposite
    print("angle:" + str(noApply))
    return noApply

def turn(Ang):
    # need rounded because dosen't return fakes
    global hub,leftMotor,rightMotor
    desiredModAng = Ang
    #desiredModAng = hub.motion_sensor.get_yaw_angle() + Ang

    desiredModAng = round(desiredModAng)
    
    if desiredModAng == 180:
        print("180 degree bruh")
        turn(90)
        turn(90)
        pass
    if desiredModAng == 0:
        pass


    leftMotor.start_at_power(30)
    rightMotor.start_at_power(30)

    shouldGo = True
    while shouldGo == True:
        curAng = hub.motion_sensor.get_yaw_angle()
        if curAng == desiredModAng:
            
            break
    leftMotor.stop()
    rightMotor.stop()


#BIG NOTE: don't make yourself do a 180 it will freeze/ break the robot


makeMap([1,1])
print("--------------------------------")
move([7,5],1)
print("--------------------------------")


