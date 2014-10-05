__author__ = 'akshay'

import serial


class SerialCommApi:
    serial = serial.Serial('/dev/AMA0', 9600, timeout=1)

    @staticmethod
    def sendMessage(message):
        SerialCommApi.serial.write(message)
