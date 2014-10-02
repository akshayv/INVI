from time import sleep
from business.deadreckoning.PositionCalculator import PositionCalculator
from business.wifi.WiFiLocationCalculator import WiFiLocationCalculator
from domain.wifi.AccessPoint import AccessPoint

__author__ = 'raghav'


class WiFiPoller:
    @staticmethod
    def poll():
        while(True):
            positionCalculator = PositionCalculator()
            x = positionCalculator.getX()
            y = positionCalculator.getY()

            a, b = WiFiPoller.checkLocation()

            if not(x-700 <= a <= x+700 and y-700 <= b <= y+700):
                print "Hang on while we recompute your location"
            sleep(5)


    def checkLocation(self):
        location_calculator = WiFiLocationCalculator()
        access_point = AccessPoint()

        nearbyAP = access_point.getNearbyAccessPoints()
        mapAP = access_point.getMapAccessPoints("COM1", 2)
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
            for item in topAPs:
                item["distance"] = location_calculator.computeDistanceFromRSSI(item["rssi"]) * 100
                coordinate = access_point.getCoordinate("COM1", 2, item["nodeId"])
                item["x"] = coordinate["x"]
                item["y"] = coordinate["y"]
            return location_calculator.computeLocation(topAPs)
        return "Unable to correct location due to weak WiFi signals"

if __name__ == "__main__":
    wifiPoller = WiFiPoller()
    print wifiPoller.checkLocation()