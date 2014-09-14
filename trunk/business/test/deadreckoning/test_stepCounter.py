from unittest import TestCase
from business.deadreckoning.StepCounter import StepCounter
from domain.deadreckoning.AccelerometerReading import AccelerometerReading

__author__ = 'akshay'


class TestStepCounter(TestCase):
    def test_isStep(self):
        stepCounter = StepCounter()
        stepCounter.isStep(AccelerometerReading(0, 0, 12), 100)
        stepCounter.isStep(AccelerometerReading(0, 0, 13), 150)
        stepCounter.isStep(AccelerometerReading(0, 0, 12), 200)
        stepCounter.isStep(AccelerometerReading(0, 0, 15), 250)
        stepCounter.isStep(AccelerometerReading(0, 0, 18), 300)
        stepCounter.isStep(AccelerometerReading(0, 0, 6), 350)
        stepCounter.isStep(AccelerometerReading(0, 0, 9), 400)
        stepCounter.isStep(AccelerometerReading(0, 0, 12), 450)
        stepCounter.isStep(AccelerometerReading(0, 0, 12), 500)
        self.assertEqual(stepCounter.getSteps(), 1)