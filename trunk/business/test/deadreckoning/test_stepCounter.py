from unittest import TestCase
from business.deadreckoning.StepCounter import StepCounter
from domain.deadreckoning.AccelerometerReading import AccelerometerReading

__author__ = 'akshay'


class TestStepCounter(TestCase):
    def test_isStep(self):
        stepCounter = StepCounter()
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.07, y = -9.34, z = -2.92)"), 705263)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -0.47, y = -8.90, z = -2.32)"), 705283)
        stepCounter.isStep(AccelerometerReading.fromString("( x = 0.07, y = -8.84, z = -1.23)"), 705301)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.40, y = -10.05, z = 1.08)"), 705320)
        stepCounter.isStep(AccelerometerReading.fromString("( x = 0.43, y = -11.78, z = 1.18)"), 705339)
        stepCounter.isStep(AccelerometerReading.fromString("( x = 0.06, y = -11.95, z = 1.78)"), 705358)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -0.23, y = -12.33, z = 1.64)"), 705395)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.53, y = -14.18, z = 1.99)"), 705414)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -4.13, y = -18.33, z = -0.10)"), 705433)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -6.70, y = -19.60, z = -2.69)"), 705452)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -5.70, y = -19.60, z = -6.47)"), 705471)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -6.26, y = -19.60, z = -7.61)"), 705490)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -4.03, y = -15.04, z = -6.11)"), 705520)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -4.26, y = -9.64, z = -3.34)"), 705540)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.56, y = -7.80, z = 0.02)"), 705558)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -2.81, y = -4.91, z = 3.81)"), 705577)
        stepCounter.isStep(AccelerometerReading.fromString("( x = 0.61, y = 1.90, z = 3.36)"), 705596)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -0.10, y = 6.73, z = 4.49)"), 705614)
        stepCounter.isStep(AccelerometerReading.fromString("( x = 0.83, y = 11.65, z = -0.42)"), 705662)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -0.46, y = 11.68, z = -2.76)"), 705681)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -0.53, y = 10.22, z = -6.43)"), 705699)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -2.79, y = 7.26, z = -9.11)"), 705719)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -3.88, y = 3.61, z = -11.32)"), 705737)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -2.80, y = 0.96, z = -13.61)"), 705757)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -1.37, y = 2.59, z = -14.08)"), 705786)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -5.32, y = 5.08, z = -8.80)"), 705806)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -9.77, y = 4.54, z = 0.10)"), 705824)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -18.45, y = -5.01, z = 11.63)"), 705843)
        stepCounter.isStep(AccelerometerReading.fromString("( x = -17.94, y = -19.60, z = 14.01)"), 705862)
        self.assertEqual(stepCounter.getSteps(), 1)