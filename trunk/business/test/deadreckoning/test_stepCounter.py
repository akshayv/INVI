from unittest import TestCase
from business.deadreckoning.StepCounter import StepCounter
from domain.deadreckoning.AccelerometerReading import AccelerometerReading

__author__ = 'akshay'


class TestStepCounter(TestCase):
    def test_isStep(self):
        StepCounter.reset()
        StepCounter.isStep(AccelerometerReading(0, 0, 12), 100)
        StepCounter.isStep(AccelerometerReading(0, 0, 13), 150)
        StepCounter.isStep(AccelerometerReading(0, 0, 12), 200)
        StepCounter.isStep(AccelerometerReading(0, 0, 15), 250)
        StepCounter.isStep(AccelerometerReading(0, 0, 18), 300)
        StepCounter.isStep(AccelerometerReading(0, 0, 6), 350)
        StepCounter.isStep(AccelerometerReading(0, 0, 9), 400)
        StepCounter.isStep(AccelerometerReading(0, 0, 12), 450)
        StepCounter.isStep(AccelerometerReading(0, 0, 12), 500)
        self.assertEqual(StepCounter.getSteps(), 1)