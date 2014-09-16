from Queue import Queue
from business.deadreckoning.PositionCalculator import PositionCalculator

__author__ = 'akshay'


class SerialQueueListener:
    queue = Queue(maxsize=0)

    positionCalculator = PositionCalculator.getInstance()

    @staticmethod
    def listen():
        while True:
            message = SerialQueueListener.queue.get(True)
            SerialQueueListener.queue.task_done()
            SerialQueueListener.positionCalculator.updatePosition(message)