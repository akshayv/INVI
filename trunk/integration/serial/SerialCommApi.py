__author__ = 'akshay'

import serial


class SerialCommApi:
    serial = serial.Serial('/dev/ttyAMA0', 115200, timeout=None)
    serial.open()
    @staticmethod
    def sendMessage(message):
        SerialCommApi.serial.write(message)
