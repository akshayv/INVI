from domain.deadreckoning.AccelerometerReading import AccelerometerReading

__author__ = 'akshay'


class StepCounter:
    __numSteps = 0

    __deltaH = 3.5
    __lastReadingTime = None
    __lastReading = None

    @staticmethod
    def isStep(accelerometerReading, currentTime):
        isStep = False
        if StepCounter.__lastReadingTime is not None and currentTime - StepCounter.__lastReadingTime <= 100:
            if abs(StepCounter.__lastReading - accelerometerReading.z) > StepCounter.__deltaH:
                isStep = True
                StepCounter.__numSteps += 1

        StepCounter.__lastReadingTime = currentTime
        StepCounter.__lastReading = accelerometerReading.z
        return isStep

    @staticmethod
    def getSteps():
        return StepCounter.__numSteps

    @staticmethod
    def reset():
        StepCounter.__numSteps = 0
        StepCounter.__lastReading = None
        StepCounter.__lastReadingTime = None