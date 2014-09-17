from threading import Thread
from unittest import TestCase
from business.deadreckoning.PositionCalculator import PositionCalculator
from business.deadreckoning.SerialQueueListener import SerialQueueListener
from business.deadreckoning.StepCounter import StepCounter
from domain.deadreckoning.AccelerometerReading import AccelerometerReading
from domain.deadreckoning.SensorReading import SensorReading

__author__ = 'akshay'


class TestSerialQueueListener(TestCase):
    def test_updatePosition(self):
        positionCalculator = PositionCalculator(0, 0, 0)
        for i in range(1):
            t = Thread(target=SerialQueueListener.listen)
            t.daemon = True
            t.start()

        SerialQueueListener.queue.put(SensorReading(AccelerometerReading(0, 0, 0), 0, 0))
        timeOffset = 100
        for i in range(50):
            if i % 2 == 0:
                SerialQueueListener.queue.put(SensorReading(AccelerometerReading(0, 0, 13), 0, timeOffset))
            elif i % 2 == 1:
                SerialQueueListener.queue.put(SensorReading(AccelerometerReading(0, 0, 6), 0, timeOffset))
            timeOffset += 100

        SerialQueueListener.queue.join()

        self.assertEqual(StepCounter().getSteps(), 25)
        self.assertAlmostEqual(positionCalculator.getX(), 25, None, None, 0.1)
        self.assertAlmostEqual(positionCalculator.getY(), 0, None, None, 0.1)
