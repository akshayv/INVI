from math import cos, sin, radians
from business.deadreckoning.StepCounter import StepCounter

__author__ = 'akshay'


class PositionCalculator:
    __curX = None
    __curY = None
    __northAt = None
    __strideLength = 1.0
    stepCounter = StepCounter()

    def __init__(self, curX, curY, northAt):
        self.__curX = curX
        self.__curY = curY
        self.__northAt = northAt

    def getX(self):
        return self.__curX

    def getY(self):
        return self.__curY

    #compassReading is the angle difference between North and current heading in degrees
    #currentTime is the time at which the reading was taken in millis
    def updatePosition(self, accelerometerReading, compassReading, currentTime):
        if self.stepCounter.isStep(accelerometerReading, currentTime) is True:
            relativeTheta = radians((self.__northAt + compassReading) % 360)
            self.__curX += self.__strideLength * cos(relativeTheta)
            self.__curY += self.__strideLength * sin(relativeTheta)
