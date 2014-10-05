import time
from business.deadreckoning.SerialQueueListener import SerialQueueListener
from domain.deadreckoning.AccelerometerReading import AccelerometerReading
from domain.deadreckoning.SensorReading import SensorReading
import serial

__author__ = 'akshay'


class SerialCommApi:

    DELIMITER = '12'
    serial = serial.Serial('/dev/AMA0', 9600, timeout=1)

    @staticmethod
    def onSerialMessage(item):
        SerialQueueListener.queue.put(item)

    @staticmethod
    def run():
        message = ""
        while True:
            bit = SerialCommApi.serial.read()
            if bit != SerialCommApi.DELIMITER:
                message += bit
            else:
                SerialCommApi.onSerialMessage(SensorReading.fromString(message))
                time.sleep(0.1)

    @classmethod
    def getMessage(cls):
        return SerialCommApi.serial.read()