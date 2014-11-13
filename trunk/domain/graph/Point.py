__author__ = 'akshay'


class Point:
    __x = 0.0
    __y = 0.0
    __id = 0
    __offset = 0.0
    __name = ""

    def __init__(self, id, x=0.0, y=0.0, name="", offset = 0.0):
        self.__x = x
        self.__y = y
        self.__id = id
        self.__offset = offset
        self.__name = name

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getOffset(self):
        return self.__offset

    def __str__(self):
        return "( nodeId = " + str(self.getId()) + ", x = " + str(self.getX()) + ", y = " + str(self.getY()) \
               + ", name = " + str(self.getName()) + ", offset =  " + str(self.getOffset()) + ")"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def fromString(stringPoint):
        stringPoint = stringPoint.replace(" )", "")
        stringPoint = stringPoint.replace("( ", "")
        array = stringPoint.split(", ")
        return Point(int(array[0].replace("nodeId = ", "")), float(array[1].replace("x = ", "")),
                     float(array[2].replace("y = ", "")), array[3].replace("name = ", ""), 0.0)


if __name__ == "__main__":
    print Point.fromString("( nodeId = 26, x = 5220.0, y = 1600.0, name = Seminar Room 11 )")