from sympy import *
from domain.wifi.AccessPoint import AccessPoint

__author__ = 'raghav'


class LocationCalculator:
    def computeTopThreeRSSI(self, apInfo):
        topThree = sorted(apInfo, key=lambda k: k['rssi'])[:3]
        return topThree

    def computeDistanceFromRSSI(self, rssi):
        """http://electronics.stackexchange.com/questions/83354/calculate-distance-from-rssi"""
        A = -20 # Received signal in dBm at 1 metre - need to calibrate this - setting it at -10 for now
        n = 3.5 # Path loss component - Ranges from 2.7 to 4.3
        distance = 10**((A - int(rssi))/(10*n))
        return distance

    def computeLocation(self, coordList):
        x, y = S('x y'.split())
        # x_a = (float(coordList[0]['x'].encode("ascii", "ignore")))
        # y_a = (float(coordList[0]['y'].encode("ascii", "ignore")))
        equations = [
            Eq((x - (float(coordList[0]['x'].encode("ascii", "ignore"))))**2 + (y - (float(coordList[0]['y'].encode("ascii", "ignore"))))**2, float(coordList[0]['distance'])**2),
            Eq((x - (float(coordList[1]['x'].encode("ascii", "ignore"))))**2 + (y - (float(coordList[1]['y'].encode("ascii", "ignore"))))**2, float(coordList[1]['distance'])**2),
            Eq((x - (float(coordList[2]['x'].encode("ascii", "ignore"))))**2 + (y - (float(coordList[2]['y'].encode("ascii", "ignore"))))**2, float(coordList[2]['distance'])**2)
        ]
        return solve(equations, [x, y])


if __name__ == "__main__":
    location_calculator = LocationCalculator()
    access_point = AccessPoint()

    nearbyAP = access_point.getNearbyAccessPoints()
    mapAP = access_point.getMapAccessPointsCoordinates()
    filteredAP = []
    for nap in nearbyAP:
        for map in mapAP:
            if access_point.checkIfBSSIDIsSame(nap['bssid'], map['bssid']):
                filteredAP.append(nap)
    # print filteredAP

    topThree = location_calculator.computeTopThreeRSSI(filteredAP)
    # print topThree
    topBssidList = []
    for ap in topThree:
        topBssidList.append(ap['bssid'])
    # print topBssidList

    mapBssidList = access_point.getMapAccessPointsBSSIDs()
    # for b in mapBssidList:
    #     print "map bssids:", b['bssid']

    coordList = []
    # print topThree
    # print mapBssidList


    for bssid in topThree:
        for b in mapBssidList:
            # print b['bssid']
            if AccessPoint.checkIfBSSIDIsSame(bssid['bssid'], b['bssid']):
                # coordinates.append({"bssid")
                coordList.append({ "nodeName": b["nodeName"], "bssid": b["bssid"], "nodeId": b["nodeId"], "rssi": bssid["rssi"] })
    # print coordList
    print location_calculator.computeDistanceFromRSSI(-39)

    for item in coordList:
        item["distance"] = location_calculator.computeDistanceFromRSSI(item["rssi"])
        coordinate = access_point.getCoordinate(item["nodeId"])
        item["x"] = coordinate["x"]
        item["y"] = coordinate["y"]

    # print coordList
    # print location_calculator.computeLocation(coordList)
    # print location_calculator.computeLocation([{'x': 0, "y": 2, "distance": 2}, {"x": 2, "y": 0, "distance": 2}, {"x": -2, "y": 0, "distance": 2}])
