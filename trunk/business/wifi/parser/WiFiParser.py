from integration.http.map.MapRetriever import MapRetriever

__author__ = 'raghav'

class WiFiParser:
    @staticmethod
    def parseWiFiAccessPoints(wifiJson):
        accessPoints = wifiJson["wifi"]
        print accessPoints

if __name__ == "__main__":
    wifiParser = WiFiParser()
    wifiJson = MapRetriever().retrieveData("DemoBuilding", 1)
    accessPoints = wifiParser.parseWiFiAccessPoints(wifiJson)
    print accessPoints