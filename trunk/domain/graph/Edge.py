from math import sqrt

__author__ = 'akshay'


class Edge:
    __sourceNode = None
    __destNode = None
    __distance = 1.0

    def __init__(self, sourceNode, destNode, distance):
        self.__sourceNode = sourceNode
        self.__destNode = destNode
        self.__distance = distance

    def getSourceNode(self):
        return self.__sourceNode

    def getDestNode(self):
        return self.__destNode

    def getDistance(self):
        return self.__distance

    def __eq__(self, other):
        if not isinstance(other, Edge):
            return False
        return self.getSourceNode().getId() == other.getSourceNode().getId() \
            and self.getDestNode().getId() == other.getDestNode().getId()

    @staticmethod
    def getDistanceBetweenPoints(point1, point2):
        return sqrt(pow(abs(float(point1.getX()) - float(point2.getX())), 2)
                    + pow(abs(float(point1.getY()) - float(point2.getY())), 2))


    def __str__(self):
        return "( source = " + str(self.getSourceNode().getId()) + ", dest = " + str(self.getDestNode().getId()) \
               + ", dist = " + str(self.getDistance()) + " )"