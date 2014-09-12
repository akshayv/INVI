from integration.http.map.MapRetriever import MapRetriever
from integration.terminal.CommandExecutor import CommandExecutor
import subprocess
import tempfile

import os

__author__ = 'raghav'

class WiFiParser:
    @staticmethod
    def parseWiFiAccessPoints(wifiJson):
        accessPoints = wifiJson["wifi"]

        # change this to iwlist scan
        command = ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport','-sNUS']

        output = CommandExecutor().executeCommand(command)
        print output

if __name__ == "__main__":
    wifiParser = WiFiParser()
    wifiJson = MapRetriever().retrieveData("DemoBuilding", 1)
    accessPoints = wifiParser.parseWiFiAccessPoints(wifiJson)
    print accessPoints