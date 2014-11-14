from math import atan2, degrees
import sys
import time
from business.deadreckoning.NorthAt import NorthAt
from domain.graph.Point import Point
from integration.earphones.EarphonesApi import EarphonesApi

__author__ = 'akshay'


class DirectionSpecifier(object):
    locationQueue = []
    nextLocation = None
    curLevelQueue = []

    UP = "straight"
    DOWN = "back"
    LEFT = "left"
    RIGHT = "right"

    STRAIGHT_LEFT = "straight-left"
    STRAIGHT_RIGHT = "straight-right"
    BACK_LEFT = "back-left"
    BACK_RIGHT = "back-right"



    weirdNodes = [{"id": "2-2-P17", "theta": 360.0}, {"id": "2-2-P2", "theta": 360.0}, {"id": "2-2-P5", "theta": 360.0},
                  {"id": "2-2-P19", "theta": 360.0}, {"id": "2-2-P6", "theta": 360.0},
                  {"id": "2-2-P1", "theta": 360.0}, {"id": "1-2-P22", "theta": 360.0}, {"id": "1-2-P39", "theta": 360.0},
                  {"id": "1-2-P17", "theta": 360.0}, {"id": "1-2-P21", "theta": 360.0}, {"id": "1-2-P24", "theta": 360.0}]

    def getWeirdTheta(self, node):
        nodeString = str(node.getBuilding()) + "-" + str(node.getLevel()) + "-" + str(node.getName())
        for weirdNode in self.weirdNodes:
            if weirdNode["id"] == nodeString:
                return weirdNode["theta"]
        return -99

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(DirectionSpecifier, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        pass

    def setLocationQueue(self, locationQueue):
        self.locationQueue = locationQueue
        if len(locationQueue) is not 0:
            temp = locationQueue.pop(0)
            self.curLevelQueue = temp["graph"]
            NorthAt().setNorthAt(temp["northAt"])
            self.nextLocation = self.curLevelQueue[0]

    def getNextHeading(self, curDir, curX, curY, northAt):
        dirInAngle = degrees(atan2((self.nextLocation.getY() - curY), (
            self.nextLocation.getX() - curX)))
        bearing = (90 - dirInAngle) % 360
        adjustedBearing = (bearing + 360 - northAt) % 360

        weirdTheta = self.getWeirdTheta(self.nextLocation)
        if weirdTheta != -99:
            delta = weirdTheta
        else:
            delta = (adjustedBearing - curDir + self.nextLocation.getOffset()) % 360
        print "Cur Dir:" + str(curDir)
        print "Delta:" + str(delta)
        return delta

    def getNextDirection(self, curX, curY, curDir, northAt):
        delta = self.getNextHeading(curDir, curX, curY, northAt)
        if 0 < delta <= 22 or 360 >= delta > 338:
            return DirectionSpecifier.UP
        elif 22 < delta <= 67:
            return DirectionSpecifier.STRAIGHT_RIGHT
        elif 67 < delta <= 112:
            return DirectionSpecifier.RIGHT
        elif 112 < delta <= 158:
            return DirectionSpecifier.BACK_RIGHT
        if 158 < delta <= 202:
            return DirectionSpecifier.DOWN
        elif 202 < delta <= 247:
            return DirectionSpecifier.BACK_LEFT
        elif 247 < delta <= 292:
            return DirectionSpecifier.LEFT
        elif 292 < delta <= 338:
            return DirectionSpecifier.STRAIGHT_LEFT

    def next(self, curX, curY, curDir):
        if abs(curX - self.nextLocation.getX()) < 100.0 and abs(
                        curY - self.nextLocation.getY()) < 100.0:
            curr = self.curLevelQueue.pop(0)
            if len(self.curLevelQueue) == 0 and len(self.locationQueue) == 0:
                EarphonesApi.outputText("You have reached your destination.")
                sys.exit()
            elif len(self.curLevelQueue) == 0 and len(self.locationQueue) != 0:
                EarphonesApi.outputText("Entering next building")
                temp = self.locationQueue.pop(0)
                NorthAt().setNorthAt(temp["northAt"])
                self.curLevelQueue = temp["graph"]
                curr = self.curLevelQueue.pop(0)
                curX = curr.getX()
                curY = curr.getY()

            self.nextLocation = self.curLevelQueue[0]
            EarphonesApi.outputText(
                "Currently at " + str(curr.getName()) + ". Moving to " + str(self.nextLocation.getName()))

        EarphonesApi.outputText(self.getNextDirection(curX, curY, curDir, NorthAt().getNorthAt()))
        return curX, curY

if __name__ == "__main__":
    locations = [{"graph":[Point.fromString("( nodeId = 26, x = 5220.0, y = 1600.0, name = Seminar Room 11 )"),
                 Point.fromString("( nodeId = 23, x = 5220.0, y = 1380.0, name = P24 )"),
                 Point.fromString("( nodeId = 27, x = 5220.0, y = 620.0, name = P28 )"),
                 Point.fromString("( nodeId = 25, x = 5220.0, y = 360.0, name = P26 )"),
                 Point.fromString("( nodeId = 21, x = 4800.0, y = 360.0, name = P22 )")], "northAt": 180}]
    directionSpecifier = DirectionSpecifier()
    directionSpecifier.setLocationQueue(locations)
    directionSpecifier.next(5220.0, 1600.0, 120)
