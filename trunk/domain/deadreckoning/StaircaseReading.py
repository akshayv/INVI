from math import floor

__author__ = 'akshay'

class StaircaseReading:
    distance = None

    def __init__(self, distance):
        self.distance = distance

    @staticmethod
    def fromString(stringReading):
        d = str(stringReading).replace("( distance = ", "")
        d = d.replace(")", "")
        return StaircaseReading(float((d)))
    def __str__(self):
        return "( distance = " + str(self.distance) + " )"


if __name__ == "__main__":
    s = StaircaseReading(13.8)
    print StaircaseReading.fromString(s)
