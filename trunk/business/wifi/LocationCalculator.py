from sympy import Eq, Line, Point, S, solve
from domain.wifi.AccessPoint import AccessPoint

__author__ = 'raghav'


class LocationCalculator:
    def computeTopThreeRSSI(self, apInfo):
        topThree = sorted(apInfo, key=lambda k: k['rssi'])[:3]
        topThreeFiltered = []
        for i in range(len(topThree)):
            if int(topThree[i]['rssi']) > -60:
                topThreeFiltered.append(topThree[i])
        return topThreeFiltered

    def computeDistanceFromRSSI(self, rssi):
        """http://electronics.stackexchange.com/questions/83354/calculate-distance-from-rssi"""
        A = -20 # Received signal in dBm at 1 metre - need to calibrate this - setting it at -10 for now
        n = 3.5 # Path loss component - Ranges from 2.7 to 4.3
        distance = 10**((A - int(rssi))/(10*n))
        return distance

    def computeLocation(self, coordList):
        x, y = S('x y'.split())
        print coordList
        x_a = float(str(coordList[0]['x']))
        x_b = float(str(coordList[1]['x']))
        y_a = float(str(coordList[0]['y']))
        y_b = float(str(coordList[1]['y']))

        if len(coordList) > 2:
            x_c = float(str(coordList[2]['x']))
            y_c = float(str(coordList[2]['y']))

        print x_a, y_a, float(coordList[0]['distance'])
        print x_b, y_b, float(coordList[1]['distance'])

        # Solve intersection of 2 circles
        equations = [
            Eq((x - x_a)**2 + (y - y_a)**2, float(coordList[0]['distance'])**2),
            Eq((x - x_b)**2 + (y - y_b)**2, float(coordList[1]['distance'])**2)
        ]

        p1, p2 = solve(equations)
        point1 = Point(p1[x], p1[y])
        point2 = Point(p2[x], p2[y])

        # Find equation of line joining circle intersections
        l = Line(point1, point2)
        c = l.coefficients

        # If 3 strong points, compute trilateration, else average two points
        if len(coordList) > 2:
            a, b = solve([
                Eq((x - x_c)**2 + (y - y_c)**2, float(coordList[2]['distance'])**2),
                c[0]*x + c[1]*y + c[2]
            ])

            ret = b
            try:
                if (((a[x] <= p1[x] and a[y] <= p2[y]) and (a[x] >= p2[x] and a[y] >= p2[y])) or
                        ((a[x] >= p1[x] and a[y] >= p2[y]) and (a[x] <= p2[x] and a[y] <= p2[y]))):
                    ret = a
            except TypeError:
                pass
            return ret
        else:
            ret = {x: (p1[x] + p2[x]) / 2, y: (p1[y] + p2[y]) / 2}
            return ret


if __name__ == "__main__":
    location_calculator = LocationCalculator()
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
        print location_calculator.computeLocation(topAPs)
