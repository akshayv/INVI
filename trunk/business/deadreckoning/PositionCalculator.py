from math import cos, sin, radians
from business.deadreckoning.StepCounter import StepCounter
from domain.deadreckoning.SensorReading import SensorReading

__author__ = 'akshay'


class PositionCalculator(object):
    __curX = None
    __curY = None
    __northAt = None
    __strideLength = 1.0
    stepCounter = StepCounter()
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(PositionCalculator, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance

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
    def updatePosition(self, sensorReading):
        if not isinstance(sensorReading, SensorReading):
            raise Exception("Data in is not sensor reading")

        if self.stepCounter.isStep(sensorReading.accelerometerReading, sensorReading.currentTime) is True:
            relativeTheta = radians((self.__northAt + sensorReading.compassReading) % 360)
            self.__curX += self.__strideLength * cos(relativeTheta)
            self.__curY += self.__strideLength * sin(relativeTheta)