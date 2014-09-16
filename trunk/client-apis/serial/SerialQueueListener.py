from Queue import Queue
from business.deadreckoning.PositionCalculator import PositionCalculator

__author__ = 'akshay'


class SerialQueueListener:
    queue = Queue(maxsize=0)

    # Assume at this point another positionCalculator has been initialized and that instance will be returned
    positionCalculator = PositionCalculator(None, None, None)

    @staticmethod
    def listen():
        while True:
            message = SerialQueueListener.queue.get(True)
            SerialQueueListener.queue.task_done()
            SerialQueueListener.positionCalculator.updatePosition(message)