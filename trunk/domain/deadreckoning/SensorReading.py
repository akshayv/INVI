from domain.deadreckoning.AccelerometerReading import AccelerometerReading

__author__ = 'akshay'


class SensorReading:
    accelerometerReading = None
    compassReading = None
    currentTime = None

    def __init__(self, accelerometerReading, compassReading, currentTime):
        self.accelerometerReading = accelerometerReading
        self.compassReading = compassReading
        self.currentTime = currentTime

    @staticmethod
    def fromString(stringReading):
        array = stringReading.split(", ")
        ax = float(array[0].replace("( accelerometerReading = ( x = ", ""))
        ay = float(array[1].replace("y = ", ""))
        az = float(array[2].replace("z = ", "").replace(")", ""))
        accelerometerReading = AccelerometerReading(ax, ay, az)
        compass = float(array[3].replace("compassReading = ", ""))
        time = long(array[4].replace("currentTime = ", "").replace(")", ""))
        return SensorReading(accelerometerReading, compass, time)

    def __str__(self):
        return "( accelerometerReading = " + str(self.accelerometerReading) + ", compassReading = " + str(
            self.compassReading) + ", currentTime = " + str(self.currentTime) + " )"


if __name__ == "__main__":
    a = AccelerometerReading(12.2, 12.1, 13.323)
    print SensorReading.fromString(str(SensorReading(a, 121, 1001011)))

