from math import cos, sin, radians
from business.deadreckoning.DirectionSpecifier import DirectionSpecifier
from business.deadreckoning.NorthAt import NorthAt
from business.deadreckoning.StepCounter import StepCounter
from domain.deadreckoning.SensorReading import SensorReading

__author__ = 'akshay'


class PositionCalculator(object):
    __curX = None
    __curY = None
    __northAt = None
    stepCounter = StepCounter()
    __instance = None

    __K_constant = 0.354
    __lastStepTime = None
    __lastStepDir = None
    __lastStepCounted = True

    directionSpecifier = DirectionSpecifier()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(PositionCalculator, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance

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

    #compassReading is the angle difference between North and current heading in degrees
    #currentTime is the time at which the reading was taken in millis
    def updatePosition(self, sensorReading):
        if not isinstance(sensorReading, SensorReading):
            raise Exception("Data in is not sensor reading")

        if self.__lastStepCounted is False\
            and sensorReading.currentTime > self.__lastStepTime + 50:

            relativeTheta = radians((90 - ((self.__northAt.getNorthAt() + self.__lastStepDir) % 360)) % 360)
            lastPeak, lastValley = self.stepCounter.getAndClearPeakAndValley()
            # step_lenth(in mts) = (Amax - Amin) ^ .25 * K
            strideLength = ((lastPeak - lastValley) ** 0.25) * self.__K_constant * 100
            self.__curX += strideLength * cos(relativeTheta)
            self.__curY += strideLength * sin(relativeTheta)
            print "CurX: " + str(self.__curX)
            print "CurY: " + str(self.__curY)
            print "Stride Length: " + str(strideLength)
            self.directionSpecifier.next(self.__curX, self.__curY, self.__lastStepDir)
            self.__lastStepCounted = True

        if (self.__lastStepTime is None or (
            sensorReading.currentTime - self.__lastStepTime) > 1000) and self.stepCounter.isStep(
                sensorReading.accelerometerReading, sensorReading.currentTime) is True:
            self.__lastStepDir = sensorReading.compassReading
            self.__lastStepTime = sensorReading.currentTime
            self.__lastStepCounted = False
