from math import sqrt

__author__ = 'akshay'


class AccelerometerReading:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "( x = " + str(self.x) + ", y = " + str(self.y) + ", z = " + str(self.z) + " )"

    @staticmethod
    def fromString(string):
        parts = str(string).split(", ")
        return AccelerometerReading(float(parts[0].replace("( x = ", "")), float(parts[1].replace("y = ", "")),
                             float(parts[2].replace("z = ", "").replace(")", "")))

    def amplitude(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))