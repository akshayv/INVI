__author__ = 'akshay'

import serial


class SerialCommApi:
    serial = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
    serial.open()
    @staticmethod
    def sendMessage(message):
        SerialCommApi.serial.write(message)