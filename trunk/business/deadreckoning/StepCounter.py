__author__ = 'akshay'


class StepCounter(object):
    _numSteps = 0

    _deltaH = 3.5
    _lastReadingTime = None
    _lastReading = None
    _lastDir = 1
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(StepCounter, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def isStep(self, accelerometerReading, currentTime):
        isStep = False
        if self._lastReadingTime is not None and currentTime - self._lastReadingTime > 100:
            self._lastReading = accelerometerReading.z
            self._lastReadingTime = currentTime
            self._lastDir = 1

        # We define a step as peak in acc. followed by a valley.
        # This block corresponds to if it is a peak.
        if self._lastDir == 1:
            if self._lastReading is None or accelerometerReading.z > self._lastReading:
                self._lastReadingTime = currentTime
                self._lastReading = accelerometerReading.z
            elif self._lastReading - accelerometerReading.z > self._deltaH:
                self._numSteps += 1
                isStep = True
                self._lastDir = 0
                self._lastReading = accelerometerReading.z
        # This blocks corresponds to if it is a valley
        elif self._lastDir == 0:
            if self._lastReading is None or accelerometerReading.z < self._lastReading:
                self._lastReadingTime = currentTime
                self._lastReading = accelerometerReading.z
            # If it was a valley but is rising and the difference if > deltaH,
            # we do not count it as a step
            elif accelerometerReading.z - self._lastReading > self._deltaH:
                self._lastDir = 1
                self._lastReading = accelerometerReading.z

        return isStep

    def getSteps(self):
        return self._numSteps

    def reset(self):
        self._numSteps = 0
        self._lastReading = None
        self._lastReadingTime = None