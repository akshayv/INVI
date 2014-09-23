from sympy import *
from domain.wifi.AccessPoint import AccessPoint

__author__ = 'raghav'


class LocationCalculator:
    def computeTopThreeStrengths(self, apInfo):
        topThree = sorted(apInfo, key=lambda k: k['ssid'], reverse=True)[:3]
        return topThree

    def computeDistanceFromSSID(self, ssid):
        A = -10 # Received signal in dBm at 1 metre - need to calibrate this - setting it at -10 for now
        n = 2.7 # Path loss component - Ranges from 2.7 to 4.3
        distance = 10**((A - ssid)/(10*n))
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
    wifiParser = LocationCalculator()
    # for ap in accessPoints:
    wifi = ""
    for ap in ["NUS"]:
        wifi = wifiParser.obtainWiFiStrength(ap)
    wifiParser.computeLocation({ "x": 2, "y": 0, "z": 0, "distance": 2 },
        { "x": 0, "y": 2, "z": 0, "distance": 2 }, { "x": -2, "y": 0, "z": 0, "distance": 2 })