from threading import Thread
from time import sleep
from SerialQueueListener import SerialQueueListener
from business.deadreckoning.PositionCalculator import PositionCalculator
from business.deadreckoning.StepCounter import StepCounter
from domain.deadreckoning.AccelerometerReading import AccelerometerReading
from domain.deadreckoning.SensorReading import SensorReading

__author__ = 'akshay'


class SerialCommApi:

    @staticmethod
    def onSerialMessage(item):
        #TODO READ SERIAL DATA FROM PORT AND BATCH AND SEND
        SerialQueueListener.queue.put(item)

if __name__ == '__main__':
    api = SerialCommApi()
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

    print StepCounter().getSteps()
    print positionCalculator.getX()
    print positionCalculator.getY()
