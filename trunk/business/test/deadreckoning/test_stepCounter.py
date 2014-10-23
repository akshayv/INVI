from unittest import TestCase
from business.deadreckoning.StepCounter import StepCounter
from domain.deadreckoning.AccelerometerReading import AccelerometerReading

__author__ = 'akshay'


class TestStepCounter(TestCase):
    def test_isStep(self):
        stepCounter = StepCounter()
        stepCounter.isStep(AccelerometerReading.fromString("( x = 9.8, y = -1.07, z = 9.8)"), 23000)
        stepCounter.isStep(AccelerometerReading.fromString("( x = 9.8, y = -1.07, z = 9.8)"), 23020)
        stepCounter.isStep(AccelerometerReading.fromString("( x = 9.8, y = -1.07, z = 9.8)"), 23040)
        stepCounter.isStep(AccelerometerReading.fromString("( x = 9.8, y = -1.07, z = 9.8)"), 23060)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -6.06, y = -1.07, z = 13.31)"), 23080)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -6.00, y = -0.32, z = 14.49)"), 23099)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -6.40, y = -0.10, z = 15.62)"), 23117)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -6.01, y = -2.43, z = 14.47)"), 23137)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.68, y = -6.35, z = 6.13)"), 23169)
        stepCounter.isStep(AccelerometerReading.fromString("( x = 3.31, y = -4.39, z = 5.38)"), 23188)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.13, y = -2.84, z = 5.09)"), 23206)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.42, y = -0.10, z = 6.38)"), 23225)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.97, y = -0.54, z = 6.64)"), 23614)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.23, y = -0.80, z = 6.42)"), 23632)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.99, y = -1.81, z = 6.49)"), 23652)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -5.72, y = -3.07, z = 13.70)"), 23698)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -10.48, y = -6.01, z = 15.61)"), 23716)
        self.assertEqual(stepCounter.getSteps(), 1)