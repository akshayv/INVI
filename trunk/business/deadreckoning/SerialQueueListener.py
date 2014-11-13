from Queue import Queue
from business.deadreckoning.PositionCalculator import PositionCalculator
from domain.deadreckoning.SensorReading import SensorReading
from domain.deadreckoning.StaircaseReading import StaircaseReading

__author__ = 'akshay'


class SerialQueueListener:
    queue = Queue(maxsize=0)

    # Assume at this point another positionCalculator has been initialized and that instance will be returned
    positionCalculator = PositionCalculator()

    @staticmethod
    def listen():
        while True:
            message = SerialQueueListener.queue.get(True)
            if isinstance(message, SensorReading):
                SerialQueueListener.positionCalculator.updatePosition(message)
            elif isinstance(message, StaircaseReading):
                SerialQueueListener.positionCalculator.updateStaircase(message)
            SerialQueueListener.queue.task_done()