__author__ = 'akshay'


class Point:
    __x = 0.0
    __y = 0.0
    __id = 0
    __name = ""

    def __init__(self, id, x=0.0, y=0.0, name=""):
        self.__x = x
        self.__y = y
        self.__id = id
        self.__name = name

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def __str__(self):
        return "( nodeId = " + str(self.getId()) +  ", x = " + str(self.getX()) + ", y = " + str(self.getY()) \
               + ", name = " + str(self.getName()) + " )"