import json

__author__ = 'akshay'

import urllib2


class MapRetriever:
    DATA_END_POINT = "http://showmyway.comp.nus.edu.sg/getMapInfo.php?"
    BUILDING_PARAMETER = "&Building="
    LEVEL_PARAMETER = "&Level="

    def retrieveData(self, building, level):
        return json.loads(urllib2.urlopen(
            self.DATA_END_POINT + self.BUILDING_PARAMETER + str(building) + self.LEVEL_PARAMETER + str(level)).read())


if __name__ == "__main__":
    mapRetriever = MapRetriever()
    jsonData = mapRetriever.retrieveData("DemoBuilding", 1)["map"]
    for doc in jsonData:
        print doc