from integration.http.map.MapRetriever import MapRetriever
from integration.terminal.CommandExecutor import CommandExecutor
from integration.terminal.Platform import Platform

__author__ = 'raghav'


class AccessPoint:
    def filterRepeatingAccessPoints(self, ap_info):
        toBeRemoved = []
        for ap1 in ap_info:
            for ap2 in ap_info:
                if ap1['bssid'] != ap2['bssid']:
                    if self.checkIfBSSIDIsSame(ap1['bssid'], ap2['bssid']):
                        ap = ap1 if int(ap1['rssi']) < int(ap2['rssi']) else ap2
                        toBeRemoved.append(ap)
        ap_info = [x for x in ap_info if x not in toBeRemoved]
        return ap_info

    def getNearbyAccessPoints(self):
        ap_info = []
        if Platform().getOS() == "OS X":
            command = ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport', '-sNUS']
            output = CommandExecutor().executeCommandWithOutput(command).split('\n')

            # Parse terminal output
            output.pop(-1) # Check for exception
            for networkInfo in output:
                networkInfo = networkInfo.lstrip().rstrip().split(" ")
                ap_info.append({ "bssid": networkInfo[1], "rssi": networkInfo[2] })
            ap_info.pop(0) # Check for exception

            # Filter similar APs
            ap_info = self.filterRepeatingAccessPoints(ap_info)

        elif Platform().getOS() == "Linux":
            pass
        return ap_info

    def getMapAccessPoints(self, building, level):
        wifiJson = MapRetriever().retrieveData(building, level)
        accessPoints = wifiJson["wifi"]
        return accessPoints

    def getCoordinate(self, building, level, nodeId):
        accessPoints = self.getMapAccessPoints(building, level)
        coordinate = {}
        for ap in accessPoints:
            if ap['nodeId'] == nodeId:
                coordinate["nodeId"] = nodeId
                coordinate["x"] = ap["x"]
                coordinate["y"] = ap["y"]
        return coordinate

    @staticmethod
    def checkIfBSSIDIsSame(bssid1, bssid2):
        if bssid1[:-2] == bssid2[:-2]:
            return True
        else:
            return False


if __name__ == "__main__":
    access_point = AccessPoint()
    # print "getMapAccessPoints:", access_point.getMapAccessPoints("COM1", 2)
    # print "checkIfBSSIDIsSame:", access_point.checkIfBSSIDIsSame("1C:DD:5E:AA:22:5B", "1C:DD:5E:AA:22:5B")
    # print "getNearbyAccessPoints:", access_point.getNearbyAccessPoints()
    # print "filterRepeatingAccessPoints:", access_point.filterRepeatingAccessPoints(access_point.getNearbyAccessPoints())

