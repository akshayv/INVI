from domain.graph.Point import Point

__author__ = 'akshay'


class Position:
    __building = None
    __level = None
    __x = None
    __y = None
    __name = None

    def __init__(self, building, level, x, y, name):
        self.__building = building
        self.__level = level
        self.__x = x
        self.__y = y
        self.__name = name

    def getBuilding(self):
        return self.__building

    def getLevel(self):
        return self.__level

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getName(self):
        return self.__name