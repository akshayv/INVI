from integration.http.map.MapRetriever import MapRetriever
from integration.terminal.CommandExecutor import CommandExecutor
from integration.terminal.Platform import Platform

__author__ = 'raghav'

class AccessPoint:
    def getNearbyAccessPoints(self):
        # TODO: asynchronous polling
        ap_info = []
        if Platform().getOS() == "OS X":
            command = ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport', '-sNUS']
            output = CommandExecutor().executeCommand(command).split('\n')
            output.pop(-1) # Check for exception
            for networkInfo in output:
                networkInfo = networkInfo.lstrip().rstrip().split(" ")
                ap_info.append({ "bssid": networkInfo[1], "ssid": networkInfo[2] })
            ap_info.pop(0) # Check for exception
        return ap_info

    def getMapAccessPoints(self):
        wifiJson = MapRetriever().retrieveData("DemoBuilding", 1)
        accessPoints = wifiJson["wifi"]
        # for item in accessPoints:
        #     ssidList.append(item["nodeName"].encode("ascii", "ignore"))
        return accessPoints

    def getMapAccessPointsCoordinates(self):
        accessPoints = self.getMapAccessPoints()
        accessPointsCoordinates = []
        for apc in accessPoints:
            accessPointsCoordinates.append({ "x": apc["x"], "y": apc["y"], "bssid": apc["macAddr"] })
        return accessPointsCoordinates

    def getMapAccessPointsBSSIDs(self):
        accessPoints = self.getMapAccessPoints()
        accessPointsBSSIDs = []
        for apc in accessPoints:
            accessPointsBSSIDs.append({ "bssid": apc["macAddr"], "nodeName": apc["nodeName"], "nodeId": apc["nodeId"] })
        return accessPointsBSSIDs

    def getCoordinate(self, nodeId):
        accessPoints = self.getMapAccessPoints()
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
    print "getMapAccessPoints: ", access_point.getMapAccessPoints()
    # print "getMapAccessPointsCoordinates: ", access_point.getMapAccessPointsCoordinates()
    # print "getMapAccessPointsBSSIDs: ", access_point.getMapAccessPointsBSSIDs()
    # print "checkIfBSSIDIsSame: ", access_point.checkIfBSSIDIsSame("1C:DD:5E:AA:22:5B", "1C:DD:5E:AA:22:5B")
    # print "getNearbyAccessPoints: ", access_point.getNearbyAccessPoints()
    print access_point.filterRepeatingAccessPoints(access_point.getNearbyAccessPoints())


