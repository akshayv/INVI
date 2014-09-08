__author__ = 'akshay'


class StepCounter:
    numSteps = 0
    deltaH = 3.5
    lastReadingTime = None
    lastReading = None

    @staticmethod
    def countSteps(accelerometerReading, currentTime):
        if StepCounter.lastReadingTime is not None and currentTime - StepCounter.lastReadingTime <= 100:
            if abs(StepCounter.lastReading - accelerometerReading) > StepCounter.deltaH:
                StepCounter.numSteps += 1

        StepCounter.lastReadingTime = currentTime
        StepCounter.lastReading = accelerometerReading


if __name__ == "__main__":
    StepCounter.countSteps(12, 100)
    StepCounter.countSteps(13, 150)
    StepCounter.countSteps(12, 200)
    StepCounter.countSteps(15, 250)
    StepCounter.countSteps(18, 300)
    StepCounter.countSteps(6, 350)
    StepCounter.countSteps(9, 400)
    StepCounter.countSteps(12, 450)
    StepCounter.countSteps(12, 500)
    print StepCounter.numSteps