import time
from integration.earphones.EarphonesApi import EarphonesApi

__author__ = 'akshay'

import RPi.GPIO as GPIO


class KeyPadApi:

    GPIO.setmode(GPIO.BOARD)
    KEYPAD = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              ['*', 0, '#']]
    #GPIO PINS
    ROW = [19, 15, 13, 11]
    COLUMN = [12, 16, 18]

    @staticmethod
    def getKey():
                 # Set all columns as output low
        for j in range(len(KeyPadApi.COLUMN)):
            GPIO.setup(KeyPadApi.COLUMN[j], GPIO.OUT)
            GPIO.output(KeyPadApi.COLUMN[j], GPIO.LOW)

        # Set all rows as input
        for i in range(len(KeyPadApi.ROW)):
            GPIO.setup(KeyPadApi.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Scan rows for pushed key/button
        # A valid key press should set "rowVal"  between 0 and 3.
        rowVal = -1
        #print rowVal
        while 0 > rowVal or rowVal > 3:
            for i in range(len(KeyPadApi.ROW)):
                tmpRead = GPIO.input(KeyPadApi.ROW[i])
                if tmpRead == 0:
                    rowVal = i

        # Convert columns to input
        for j in range(len(KeyPadApi.COLUMN)):
                GPIO.setup(KeyPadApi.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Switch the i-th row found from scan to output
        GPIO.setup(KeyPadApi.ROW[rowVal], GPIO.OUT)
        GPIO.output(KeyPadApi.ROW[rowVal], GPIO.HIGH)

        # Scan columns for still-pushed key/button
        # A valid key press should set "colVal"  between 0 and 2.
        colVal = -1
        while 0 > colVal or colVal > 2:
            for j in range(len(KeyPadApi.COLUMN)):
                tmpRead = GPIO.input(KeyPadApi.COLUMN[j])
                if tmpRead == 1:
                    colVal=j

        time.sleep(0.5)
	print KeyPadApi.KEYPAD[rowVal][colVal]
        return KeyPadApi.KEYPAD[rowVal][colVal]


    @staticmethod
    def getLevel():
        levelStr = ""
        key = ''
        EarphonesApi.outputText("Please enter the level followed by a hash")
        while True:
            key = KeyPadApi.getKey()
            if key is not '#':
		levelStr += str(key)
	    else:
		break
        return levelStr

    @staticmethod
    def getLocation(possibleLocations):
        EarphonesApi.outputText(
            "The locations will now be specified to you with a number. Please enter the corresponding number when we ask for it")
        locNum = {}
        for i in range(len(possibleLocations)):
            EarphonesApi.outputText(i)
            EarphonesApi.outputText(possibleLocations[i].getName())
            time.sleep(0.2)
            locNum[i] = possibleLocations[i]

        EarphonesApi.outputText("Please enter the number followed by hash")
        num = ""
        key = ''
        while True:
            key = KeyPadApi.getKey()
	    if key is not '#':
            	num += str(key)
	    else:
		break
        return locNum[int(num)]

    @staticmethod
    def getConfirmation():
        EarphonesApi.outputText(
            "To confirm press 1")
        key = KeyPadApi.getKey()
        return key == 1

    @staticmethod
    def getBuilding():
        num = ""
        locations = ["COM1", "COM2"]
        EarphonesApi.outputText(
            "The buildings will now be specified to you with a number. Please enter the corresponding number when we ask for it")
        locNum = {}
        for i in range(len(locations)):
            EarphonesApi.outputText(i)
            EarphonesApi.outputText(locations[i])
            time.sleep(0.2)
            locNum[i] = locations[i]
        EarphonesApi.outputText("Please enter the building number followed by a hash")
        num = ""
        key = ''
        while True:
            key = KeyPadApi.getKey()
	    if key is not '#':
            	num += str(key)
	    else:
		break
	if int(num) > len(locations) - 1:
	    raise Exception("No such option")
	return locNum[int(num)]


if __name__ == "__main__":
    print KeyPadApi.getKey()




