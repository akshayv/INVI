from integration.http.map.MapRetriever import MapRetriever
from integration.terminal.CommandExecutor import CommandExecutor

__author__ = 'raghav'

class WiFiParser:
    @staticmethod
    def obtainWiFiAccessPoints(wifiJson):
        accessPoints = wifiJson["wifi"]
        ssidList = []
        for item in accessPoints:
            ssidList.append(item["nodeName"].encode("ascii", "ignore"))
        return ssidList

    @staticmethod
    def obtainWiFiStrength(ssid):
        command = ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport','-s'+ssid]
        output = CommandExecutor().executeCommand(command)
        return output
    @staticmethod
    def calculateDistanceFromStrength(strength):
        # obtain distance from strength
        A = -10 # Received signal in dBm at 1 metre - need to calibrate this - setting it at -10 for now
        n = 2.7 # Path loss component - Ranges from 2.7 to 4.3
        distance = 10**((A - strength)/(10*n))
        return distance

    @staticmethod
    def calculateLocation(coord_a, coord_b, coord_c):
        # solve equations to return a range of points
        x, y, z = S('x y z'.split())
        equations = [
            Eq((x - coord_a['x'])**2 + (y - coord_a['y'])**2 + (z - coord_a['z'])**2, coord_a['distance']**3),
            Eq((x - coord_b['x'])**2 + (y - coord_b['y'])**2 + (z - coord_b['z'])**2, coord_b['distance']**2),
            Eq((x - coord_c['x'])**2 + (y - coord_c['y'])**2 + (z - coord_c['z'])**2, coord_c['distance']**2)
        ]
        print solve(equations, [x, y, z])
        # print x, y

if __name__ == "__main__":
    wifiParser = WiFiParser()
    wifiJson = MapRetriever().retrieveData("DemoBuilding", 1)
    accessPoints = wifiParser.obtainWiFiAccessPoints(wifiJson)
    # for ap in accessPoints:
    wifi = ""
    for ap in ["NUS"]:
        wifi = wifiParser.obtainWiFiStrength(ap)
    wifiParser.calculateLocation({ "x": 2, "y": 0, "z": 0, "distance": 2 },
        { "x": 0, "y": 2, "z": 0, "distance": 2 }, { "x": -2, "y": 0, "z": 0, "distance": 2 })