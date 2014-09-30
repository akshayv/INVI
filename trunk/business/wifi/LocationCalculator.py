from sympy import *
from domain.wifi.AccessPoint import AccessPoint

__author__ = 'raghav'


class LocationCalculator:
    def computeTopThreeRSSI(self, apInfo):
        topThree = sorted(apInfo, key=lambda k: k['rssi'])[:3]
        return topThree

    def computeDistanceFromRSSI(self, rssi):
        A = -10 # Received signal in dBm at 1 metre - need to calibrate this - setting it at -10 for now
        n = 2.7 # Path loss component - Ranges from 2.7 to 4.3
        distance = 10**((A - int(rssi))/(10*n))
        return distance

    def computeLocation(self, coord_a, coord_b, coord_c):
        x, y, z = S('x y z'.split())
        equations = [
            Eq((x - coord_a['x'])**2 + (y - coord_a['y'])**2 + (z - coord_a['z'])**2, coord_a['distance']**3),
            Eq((x - coord_b['x'])**2 + (y - coord_b['y'])**2 + (z - coord_b['z'])**2, coord_b['distance']**2),
            Eq((x - coord_c['x'])**2 + (y - coord_c['y'])**2 + (z - coord_c['z'])**2, coord_c['distance']**2)
        ]
        return solve(equations, [x, y, z])


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
    # print "top 3 bssids:", topBssidList
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
    print coordList
    print location_calculator.computeDistanceFromRSSI(-50)
    # print coordList
    for item in coordList:
        item["distance"] = location_calculator.computeDistanceFromRSSI(item["rssi"])
        coordinate = access_point.getCoordinate(item["nodeId"])
        item["x"] = coordinate["x"]
        item["y"] = coordinate["y"]

    # print coordList
    print location_calculator.computeLocation(coordList)

    # print location_calculator.computeLocation([{'x': 0, "y": 2, "distance": 2}, {"x": 2, "y": 0, "distance": 2}, {"x": -2, "y": 0, "distance": 2}])

