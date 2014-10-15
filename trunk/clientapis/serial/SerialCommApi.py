import time
from business.deadreckoning.SerialQueueListener import SerialQueueListener
from domain.deadreckoning.AccelerometerReading import AccelerometerReading
from domain.deadreckoning.SensorReading import SensorReading
import serial

__author__ = 'akshay'


class SerialCommApi:

    serial = serial.Serial('/dev/ttyAMA0', 9600, timeout=None)
    serial.open()
    @staticmethod
    def onSerialMessage(item):
        SerialQueueListener.queue.put(item)

    @staticmethod
    def run():
        while True:
            try:
                inp = SerialCommApi.serial.readline()
	        print inp
                SerialCommApi.onSerialMessage(SensorReading.fromString(inp))
            except Exception:
		print "ERROR DATA"

    @classmethod
    def getMessage(cls):
        return SerialCommApi.serial.readline().replace("\n", "").strip()

if __name__ == "__main__":
	SerialCommApi.run()
