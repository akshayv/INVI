from business.deadreckoning.SerialQueueListener import SerialQueueListener
from domain.deadreckoning.SensorReading import SensorReading
import serial

__author__ = 'akshay'


class SerialCommApi:
    serial = serial.Serial('/dev/ttyAMA0', 115200, timeout=None)
    serial.open()

    @staticmethod
    def onSerialMessage(item):
        SerialQueueListener.queue.put(item)

    @staticmethod
    def run():
        while True:
            try:
                inp = SerialCommApi.serial.readline()
                rawReading = SensorReading.fromString(inp)
                inp = SerialCommApi.serial.readline()
                rawReading.currentTime = long(inp)
                SerialCommApi.onSerialMessage(rawReading)
            except Exception:
                print "ERROR DATA"

    @classmethod
    def getMessage(cls):
        return SerialCommApi.serial.readline().replace("\n", "").strip()


if __name__ == "__main__":
    SerialCommApi.run()
