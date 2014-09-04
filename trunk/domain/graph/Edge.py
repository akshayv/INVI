__author__ = 'akshay'


class Edge:
    __sourceNodeId = None
    __destNodeId = None
    __distance = 1.0

    def __init__(self, sourceNodeId, destNodeId, distance):
        self.__sourceNodeId = sourceNodeId
        self.__destNodeId = destNodeId
        self.__distance = distance

    def getSourceNodeId(self):
        return self.__sourceNodeId

    def getDestNodeId(self):
        return self.__destNodeId

    def getDistance(self):
        return self.__distance

    def __eq__(self, other):
        if not isinstance(other, Edge):
            return False
        return self.getSourceNodeId() == other.getSourceNodeId() and self.getDestNodeId() == other.getDestNodeId()

    def __str__(self):
        return "( source = " + str(self.getSourceNodeId()) + ", dest = " + str(self.getDestNodeId()) \
               + ", dist = " + str(self.getDistance()) + " )"