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

        building = None
        level = None

        # Obtain BSSID, Building, Level details of all maps
        map_com1_level2 = access_point.getMapAccessPoints(1, 2)
        map_com2_level3 = access_point.getMapAccessPoints(2, 3)
        map_com2_level2 = access_point.getMapAccessPoints(2, 2)


        # Check top AP with all the store access points in all levels of all buildings
        maps = [map_com1_level2, map_com2_level3, map_com2_level2]
        location = None
        for ap in nearbyAP:
            for map in maps:
                for mapAP in map:
                    if access_point.checkIfBSSIDIsSame(ap['bssid'], mapAP['bssid']):
                        location = map


        # Determine level and building
        if location == map_com2_level2:
            building = 2
            level = 2
        elif location == map_com2_level3:
            building = 2
            level = 3
        elif location == map_com1_level2:
            building = 1
            level = 2


        filteredAP = []
        for nap in nearbyAP:
            for map in location:
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