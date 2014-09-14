from unittest import TestCase
from business.deadreckoning.PositionCalculator import PositionCalculator
from business.deadreckoning.StepCounter import StepCounter
from domain.deadreckoning.AccelerometerReading import AccelerometerReading

__author__ = 'akshay'


class TestPositionCalculator(TestCase):
    def test_updatePosition(self):
        positionCalculator = PositionCalculator(0, 0, 90)
        positionCalculator.updatePosition(AccelerometerReading(0, 0, 0), 0, 0)
        positionCalculator.updatePosition(AccelerometerReading(0, 0, 13), 0, 100)
        positionCalculator.updatePosition(AccelerometerReading(0, 0, 6), 0, 200)
        positionCalculator.updatePosition(AccelerometerReading(0, 0, 13), 0, 300)
        positionCalculator.updatePosition(AccelerometerReading(0, 0, 6), 0, 400)
        positionCalculator.updatePosition(AccelerometerReading(0, 0, 13), 0, 500)
        positionCalculator.updatePosition(AccelerometerReading(0, 0, 6), 0, 600)
        positionCalculator.updatePosition(AccelerometerReading(0, 0, 13), 0, 700)
        positionCalculator.updatePosition(AccelerometerReading(0, 0, 6), 0, 800)
        self.assertAlmostEqual(positionCalculator.getX(), 0, None, None, 0.1)
        self.assertAlmostEqual(positionCalculator.getY(), 4, None, None, 0.1)
