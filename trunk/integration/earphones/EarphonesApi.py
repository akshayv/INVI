__author__ = 'akshay'

import pyttsx


class EarphonesApi():

    @staticmethod
    def outputText(text, rate=150):
        engine = pyttsx.init()
        engine.setProperty("rate", rate)
        engine.say(text)
        engine.runAndWait()



if __name__ == "__main__":
    while True:
        earphonesApi = EarphonesApi()
        earphonesApi.outputText("Go right in 3 meters!", 250)