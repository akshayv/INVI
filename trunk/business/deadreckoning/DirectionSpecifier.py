from math import sqrt, atan2, degrees
from domain.graph.Point import Point
from integration.earphones.EarphonesApi import EarphonesApi

__author__ = 'akshay'


class DirectionSpecifier(object):
    locationQueue = []
    nextLocation = None

    UP = "straight"
    DOWN = "back"
    LEFT = "left"
    RIGHT = "right"

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(DirectionSpecifier, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, locationQueue):
        self.locationQueue = locationQueue
        if len(locationQueue) is not 0:
            self.nextLocation = locationQueue[0]

    def getNextDirection(self, curX, curY, curDir, northAt):
        dirInAngle = degrees(atan2((self.nextLocation.getY() - curY), (
            self.nextLocation.getX() - curX)))
        bearing = (90 - dirInAngle) % 360
        adjustedBearing = (bearing + 360 - northAt) % 360

        delta = (adjustedBearing - curDir) % 360
        if 0 < delta <= 45 or 360 > delta > 315:
            return DirectionSpecifier.UP
        elif 45 < delta <= 135:
            return DirectionSpecifier.RIGHT
        elif 135 < delta <= 225:
            return DirectionSpecifier.DOWN
        elif 225 < delta <= 315:
            return DirectionSpecifier.LEFT

    def next(self, curX, curY, curDir, northAt):
        if abs(curX - self.nextLocation.getX()) < 3.0 and abs(
                        curY - self.nextLocation.getY()) < 3.0:
            curr = self.locationQueue.pop(0)
            self.nextLocation = self.locationQueue[0]
            EarphonesApi.outputText(
                "You are currently at " + str(curr.getName()) + ". Moving to " + str(self.nextLocation.getName()))

        EarphonesApi.outputText("Move one step " + self.getNextDirection(curX, curY, curDir, northAt))


if __name__ == "__main__":
    locations = [Point.fromString("( nodeId = 26, x = 5220.0, y = 1600.0, name = Seminar Room 11 )"),
                 Point.fromString("( nodeId = 23, x = 5220.0, y = 1380.0, name = P24 )"),
                 Point.fromString("( nodeId = 27, x = 5220.0, y = 620.0, name = P28 )"),
                 Point.fromString("( nodeId = 25, x = 5220.0, y = 360.0, name = P26 )"),
                 Point.fromString("( nodeId = 21, x = 4800.0, y = 360.0, name = P22 )")]
    directionSpecifier = DirectionSpecifier(locations)
    directionSpecifier.next(5220.0, 1600.0, 120, 180)
