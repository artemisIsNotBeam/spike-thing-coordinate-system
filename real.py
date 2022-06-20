from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

corPlane = []
tot = [x: 6, y: 6]

# make sure tot and scale factor work toghther
startPoint = [1,1]
scaleFactor = 1 in


def makeMap():
    global corPlane, tot
    x = tot.x
    y = tot.y

    for xPlace in x:
#0 is nothing there, 1 is where we are
