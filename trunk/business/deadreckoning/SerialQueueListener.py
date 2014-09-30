from Queue import Queue
import time
from business.deadreckoning.PositionCalculator import PositionCalculator

__author__ = 'akshay'


class SerialQueueListener:
    queue = Queue(maxsize=0)

    # Assume at this point another positionCalculator has been initialized and that instance will be returned
    positionCalculator = PositionCalculator()

    @staticmethod
    def listen():
        while True:
            message = SerialQueueListener.queue.get(True)
            SerialQueueListener.positionCalculator.updatePosition(message)
            SerialQueueListener.queue.task_done()
            time.sleep(0.1)