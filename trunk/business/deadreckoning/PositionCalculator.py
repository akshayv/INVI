from math import cos, sin, radians
import math
from business.deadreckoning.DirectionSpecifier import DirectionSpecifier
from business.deadreckoning.NorthAt import NorthAt
from business.deadreckoning.StepCounter import StepCounter
from domain.deadreckoning.SensorReading import SensorReading
from integration.earphones.EarphonesApi import EarphonesApi
from integration.keypad.KeyPadApi import KeyPadApi
from integration.serial.SerialCommApi import SerialCommApi

__author__ = 'akshay'


class PositionCalculator(object):
    __curX = None
    __curY = None
    __northAt = None
    stepCounter = StepCounter()
    __instance = None
    __strideLength = 58.0
    __K_constant = 0.354
    __lastStepTime = None

    directionSpecifier = DirectionSpecifier()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(PositionCalculator, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance

    def updateStaircase(self, staircaseReading):
        EarphonesApi.outputText(
            "Staircase straight ahead in " + str(math.floor(staircaseReading.distance)) + " centimeters")
        EarphonesApi.outputText("No instructions until after you are done climbing it")
        KeyPadApi.getKey()
        self.__curX = self.directionSpecifier.nextLocation.getX()
        self.__curX = self.directionSpecifier.nextLocation.getY()
        SerialCommApi.sendMessage('1')
        self.directionSpecifier.next(self.__curX, self.__curY, 0)

    def __init__(self, curX=None, curY=None, northAt=None):
        if curX is not None:
            self.__curX = curX
        if curY is not None:
            self.__curY = curY
        if northAt is not None:
            self.__northAt = NorthAt(northAt)

    def getX(self):
        return self.__curX

    def getY(self):
        return self.__curY

    def getNorthAt(self):
        return self.__northAt.getNorthAt()

    def setX(self, value):
        self.__curX = value

    def setY(self, value):
        self.__curY = value

    #compassReading is the angle difference between North and current heading in degrees
    #currentTime is the time at which the reading was taken in millis
    def updatePosition(self, sensorReading):
        if not isinstance(sensorReading, SensorReading):
            raise Exception("Data in is not sensor reading")

        if (self.__lastStepTime is None or (
            sensorReading.currentTime - self.__lastStepTime) > 1000) and self.stepCounter.isStep(
                sensorReading.accelerometerReading, sensorReading.currentTime) is True:

            relativeTheta = radians((90 - ((self.__northAt.getNorthAt() + sensorReading.compassReading) % 360)) % 360)
            lastPeak, lastValley = self.stepCounter.getAndClearPeakAndValley()
            # step_lenth(in mts) = (Amax - Amin) ^ .25 * K
            # strideLength = ((lastPeak - lastValley) ** 0.25) * self.__K_constant * 100
            strideLength = self.__strideLength
	    self.__curX += strideLength * cos(relativeTheta)
            self.__curY += strideLength * sin(relativeTheta)
            print "CurX: " + str(self.__curX)
            print "CurY: " + str(self.__curY)
            print "Stride Length: " + str(strideLength)
            self.__curX, self.__curY = self.directionSpecifier.next(self.__curX, self.__curY, sensorReading.compassReading)
            self.__lastStepCounted = True
