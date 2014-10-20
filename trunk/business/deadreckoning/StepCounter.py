__author__ = 'akshay'


class StepCounter(object):
    __numSteps = 0

    __deltaH = 3.5
    __lastReadingTime = None
    __lastReading = None
    __lastDir = 1
    __instance = None


    __lastPeak = 0
    __lastValley = 100

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(StepCounter, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance

    def isStep(self, accelerometerReading, currentTime):
        isStep = False
        amplitude = accelerometerReading.amplitude()
        if self.__lastReadingTime is not None and currentTime - self.__lastReadingTime > 100:
            self.__lastReading = amplitude
            self.__lastReadingTime = currentTime
            self.__lastDir = 1

        # We define a step as peak in acc. followed by a valley.
        # This block corresponds to if it is a peak.
        if self.__lastDir == 1:
            if self.__lastReading is None or amplitude > self.__lastReading:
                self.__lastReadingTime = currentTime
                self.__lastReading = amplitude
            elif self.__lastReading - amplitude > self.__deltaH:
                self.__numSteps += 1
                isStep = True
                self.__lastDir = 0
                self.__lastReading = amplitude
        # This blocks corresponds to if it is a valley
        elif self.__lastDir == 0:
            if self.__lastReading is None or amplitude < self.__lastReading:
                self.__lastReadingTime = currentTime
                self.__lastReading = amplitude
            # If it was a valley but is rising and the difference if > deltaH,
            # we do not count it as a step
            elif amplitude - self.__lastReading > self.__deltaH:
                self.__lastDir = 1
                self.__lastReading = amplitude

        if amplitude > self.__lastPeak:
            self.__lastPeak = amplitude
        elif amplitude < self.__lastValley:
            self.__lastValley = amplitude

        return isStep

    def getSteps(self):
        return self.__numSteps

    def getAndClearPeakAndValley(self):
        p = self.__lastPeak
        v = self.__lastValley
        self.__lastPeak = 0
        self.__lastValley = 100
        return p, v

    def reset(self):
        self.__numSteps = 0
        self.__lastReading = None
        self.__lastReadingTime = None