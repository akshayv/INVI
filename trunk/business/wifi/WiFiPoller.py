from time import sleep
from business.deadreckoning.PositionCalculator import PositionCalculator
from business.wifi.WiFiLocationCalculator import WiFiLocationCalculator
from integration.earphones.EarphonesApi import EarphonesApi
from domain.wifi.AccessPoint import AccessPoint

__author__ = 'raghav'


class WiFiPoller:
    @staticmethod
    def poll():
        while(True):
            # EarphonesApi.outputText("WiFi is online")
            positionCalculator = PositionCalculator()
            x = positionCalculator.getX()
            y = positionCalculator.getY()

            a, b = WiFiPoller.checkLocation()
            if type(a) == str:
                # EarphonesApi.outputText(a)
                print a

            if not(x-700 <= a <= x+700 and y-700 <= b <= y+700):
                EarphonesApi.outputText("You are the wrong location! Setting you to the right location now...")
                positionCalculator.setX(a)
                positionCalculator.setY(b)
            sleep(5)

    @staticmethod
    def checkLocation():
        location_calculator = WiFiLocationCalculator()
        access_point = AccessPoint()

        nearbyAP = access_point.getNearbyAccessPoints()

        # For Week 11 demo
        building = "1"
        level = 2
        mapAP = access_point.getMapAccessPoints(building, level)
        filteredAP = []
        for nap in nearbyAP:
            for map in mapAP:
                if access_point.checkIfBSSIDIsSame(nap['bssid'], map['macAddr']):
                    nap["nodeName"] = map["nodeName"]
                    nap["bssid"] = map["macAddr"]
                    nap["nodeId"] = map["nodeId"]
                    filteredAP.append(nap)

        topAPs = location_calculator.computeTopThreeRSSI(filteredAP)

        # Compute location only if there are at least 2 strong rssi
        if len(topAPs) >= 2:
            EarphonesApi.outputText("Correcting location using WiFi")
            for item in topAPs:
                item["distance"] = location_calculator.computeDistanceFromRSSI(item["rssi"]) * 100
                coordinate = access_point.getCoordinate("COM1", 2, item["nodeId"])
                item["x"] = coordinate["x"]
                item["y"] = coordinate["y"]
            return location_calculator.computeLocation(topAPs)
        return "Unable to correct location due to weak WiFi signals", None

if __name__ == "__main__":
    wifiPoller = WiFiPoller()
    print wifiPoller.checkLocation()