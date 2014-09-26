import time
from business.deadreckoning.SerialQueueListener import SerialQueueListener
from domain.deadreckoning.AccelerometerReading import AccelerometerReading
from domain.deadreckoning.SensorReading import SensorReading

__author__ = 'akshay'


class SerialCommApi:

    @staticmethod
    def onSerialMessage(item):
        SerialQueueListener.queue.put(item)

    @staticmethod
    def run():
        while True:
            # TODO: iter = api.poll
            SerialCommApi.onSerialMessage(SensorReading(AccelerometerReading(0, 0 ,0), 100, 100))
            time.sleep(0.1)