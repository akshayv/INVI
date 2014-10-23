from unittest import TestCase
from business.deadreckoning.StepCounter import StepCounter
from domain.deadreckoning.AccelerometerReading import AccelerometerReading

__author__ = 'akshay'


class TestStepCounter(TestCase):
    def test_isStep(self):
        stepCounter = StepCounter()
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.56, y = -0.18, z = 6.68)"), 639709)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.48, y = 0.76, z = 7.68)"), 639757)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -4.31, y = -0.87, z = 7.10)"), 639823)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.97, y = -0.66, z = 8.43)"), 639873)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -4.44, y = 0.12, z = 10.69)"), 639921)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -4.75, y = 0.13, z = 10.33)"), 639988)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -5.47, y = 0.82, z = 12.19)"), 640036)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.04, y = 5.73, z = 9.89)"), 640086)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.67, y = 2.32, z = 10.15)"), 640142)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -4.99, y = 0.94, z = 9.55)"), 640191)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.66, y = 0.91, z = 7.62)"), 640240)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.54, y = 1.47, z = 7.76)"), 640293)
        stepCounter.isStep(AccelerometerReading.fromString("( x = 0.43, y = 0.67, z = 8.26)"), 640343)
        stepCounter.isStep(AccelerometerReading.fromString("( x = 0.16, y = 0.56, z = 7.22)"), 640391)
        stepCounter.isStep(AccelerometerReading.fromString("( x = 0.36, y = -1.79, z = 8.04)"), 640457)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -0.28, y = -1.65, z = 11.93)"), 640506)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.57, y = 0.44, z = 14.47)"), 640555)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.95, y = 2.64, z = 12.18)"), 640621)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.73, y = 2.95, z = 7.02)"), 640670)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.90, y = -0.48, z = 6.45)"), 640719)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.56, y = -0.18, z = 6.68)"), 639709)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.48, y = 0.76, z = 7.68)"), 639757)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -4.31, y = -0.87, z = 7.10)"), 639823)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.97, y = -0.66, z = 8.43)"), 639873)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -4.44, y = 0.12, z = 10.69)"), 639921)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -4.75, y = 0.13, z = 10.33)"), 639988)
        self.assertEqual(stepCounter.getSteps(), 1)