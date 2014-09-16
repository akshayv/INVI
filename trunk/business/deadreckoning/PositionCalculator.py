from math import cos, sin, radians
from business.deadreckoning.StepCounter import StepCounter
from domain.deadreckoning.SensorReading import SensorReading

__author__ = 'akshay'


class PositionCalculator(object):
    _curX = None
    _curY = None
    _northAt = None
    _strideLength = 1.0
    stepCounter = StepCounter()
    _instance = None

    @staticmethod
    def getInstance():
        if PositionCalculator._instance is not None:
            return PositionCalculator._instance
        else:
            raise Exception("No instance available to return")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PositionCalculator, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self, curX, curY, northAt):
        self._curX = curX
        self._curY = curY
        self._northAt = northAt

    def getX(self):
        return self._curX

    def getY(self):
        return self._curY

    #compassReading is the angle difference between North and current heading in degrees
    #currentTime is the time at which the reading was taken in millis
    def updatePosition(self, sensorReading):
        if not isinstance(sensorReading, SensorReading):
            raise Exception("Bad data in")

        if self.stepCounter.isStep(sensorReading.accelerometerReading, sensorReading.currentTime) is True:
            relativeTheta = radians((self._northAt + sensorReading.compassReading) % 360)
            self._curX += self._strideLength * cos(relativeTheta)
            self._curY += self._strideLength * sin(relativeTheta)
