from business.cache.GraphCache import GraphCache
from domain.graph.Position import Position
from integration.earphones.EarphonesApi import EarphonesApi
from integration.keypad.KeyPadApi import KeyPadApi

__author__ = 'akshay'


class LocationRetriever:

    @staticmethod
    def getLocation():

        building = None
        level = 0
        nodeId=None

        confirmation = False
        while not confirmation:
            building, level, nodeId = KeyPadApi.getLocation()
            EarphonesApi.outputText("You have input " + building + ", " + level + ", " + nodeId + ". Is this correct?", 200)
            confirmation = KeyPadApi.getConfirmation()

        EarphonesApi.outputText("Retrieving graph now.", 200)
        graphCache = GraphCache()
        floorGraph = graphCache.getGraph(building, level)
        if len(floorGraph.edges) == 0:
            raise Exception("Looks like there is no such location. Try again")

        point = floorGraph.pointsIdMap.get(int(nodeId) - 1)
        position = Position(building, level, point.getX(), point.getY(), point.getName())
        return position


    @staticmethod
    def getInitialLocation():
        EarphonesApi.outputText("Please specify initial position")
        return LocationRetriever.getLocation()

    @staticmethod
    def getDestination():
        EarphonesApi.outputText("Please specify destination")
        return LocationRetriever.getLocation()


if __name__ == "__main__":
    LocationRetriever.getInitialLocation()