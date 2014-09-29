import time
from integration.earphones.EarphonesApi import EarphonesApi

__author__ = 'akshay'

import RPi.GPIO as GPIO


class KeyPadApi:
    @staticmethod
    def setup():
        global MATRIX, ROW, COL, j
        MATRIX = [[1, 2, 3, 'A'],
                  [4, 5, 6, 'B'],
                  [7, 8, 9, 'C'],
                  ['*', 0, '#', 'D']]
        #GPIO PINS
        ROW = [7, 11, 13, 15]
        COL = [12, 16, 18, 22]
        GPIO.setMode(GPIO.BOARD)
        for j in range(4):
            GPIO.setup(COL[j], GPIO.OUT)
            GPIO.output(COL[j], 1)
        for j in range(4):
            GPIO.setup(ROW[j], GPIO.IN, pull_up_down=GPIO.PUT_UP)

    @staticmethod
    def getLevel():
        KeyPadApi.setup()
        levelStr = ""
        EarphonesApi.outputText("Please enter the level followed by a hash")
        try:
            while True:
                for j in range(4):
                    GPIO.output(COL[j], 0)
                    for i in range(4):
                        if GPIO.input(ROW[i]) == 0:
                            if MATRIX[i][j] != '#':
                                levelStr += str(MATRIX[i][j])
                            else:
                                GPIO.cleanup()
                                return int(levelStr)

                            while GPIO.input(ROW[i]) == 0:
                                pass
        except KeyboardInterrupt:
            GPIO.cleanup()

    @staticmethod
    def getLocation(possibleLocations):
        KeyPadApi.setup()
        num = ""
        EarphonesApi.outputText(
            "The locations will now be specified to you with a number. Please enter the corresponding number when we ask for it")
        locNum = {}
        for i in range(len(possibleLocations)):
            EarphonesApi.outputText(i)
            EarphonesApi.outputText(possibleLocations.getName())
            time.sleep(0.2)
            locNum[i] = possibleLocations.getName()

        EarphonesApi.outputText("Please enter the number followed by hash")
        try:
            while True:
                for j in range(4):
                    GPIO.output(COL[j], 0)
                    for i in range(4):
                        if GPIO.input(ROW[i]) == 0:
                            if MATRIX[i][j] != '#':
                                num += str(MATRIX[i][j])
                            else:
                                GPIO.cleanup()
                                return locNum[num]

                            while GPIO.input(ROW[i]) == 0:
                                pass
        except KeyboardInterrupt:
            GPIO.cleanup()

    @staticmethod
    def getConfirmation():
        KeyPadApi.setup()
        EarphonesApi.outputText(
            "To confirm press 1")
        try:
            while True:
                for j in range(4):
                    GPIO.output(COL[j], 0)
                    for i in range(4):
                        if GPIO.input(ROW[i]) == 0:
                            if MATRIX[i][j] == 1:
                                return True
                            else:
                                return False
        except KeyboardInterrupt:
            GPIO.cleanup()

    @staticmethod
    def getBuilding():
        KeyPadApi.setup()
        num = ""
        locations = ["COM1", "COM2"]
        EarphonesApi.outputText(
            "The buildings will now be specified to you with a number. Please enter the corresponding number when we ask for it")
        locNum = {}
        for i in range(len(locations)):
            EarphonesApi.outputText(i)
            EarphonesApi.outputText(locations)
            time.sleep(0.2)
            locNum[i] = locations
        EarphonesApi.outputText("Please enter the building followed by a hash")
        try:
            while True:
                for j in range(4):
                    GPIO.output(COL[j], 0)
                    for i in range(4):
                        if GPIO.input(ROW[i]) == 0:
                            if MATRIX[i][j] != '#':
                                num += str(MATRIX[i][j])
                            else:
                                GPIO.cleanup()
                                return locNum[num]

                            while GPIO.input(ROW[i]) == 0:
                                pass
        except KeyboardInterrupt:
            GPIO.cleanup()







