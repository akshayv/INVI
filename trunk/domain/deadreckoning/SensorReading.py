__author__ = 'akshay'


class SensorReading:
    accelerometerReading = None
    compassReading = None
    currentTime = None

    def __init__(self, accelerometerReading, compassReading, currentTime):
        self.accelerometerReading = accelerometerReading
        self.compassReading = compassReading
        self.currentTime = currentTime


