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
        location = None

        confirmation = False
        while not confirmation:
            EarphonesApi.outputText("Please specify Building Name")
            building = KeyPadApi.getBuilding()
            EarphonesApi.outputText("You have input " + building + ". Is this correct?")
            confirmation = KeyPadApi.getConfirmation()

        confirmation = False
        while not confirmation:
            EarphonesApi.outputText("Please specify Level")
            level = KeyPadApi.getLevel()
            EarphonesApi.outputText("You have input " + level + ". Is this correct?")
            confirmation = KeyPadApi.getConfirmation()

        EarphonesApi.outputText("Retrieving graph now.")
        graphCache = GraphCache()
        floorGraph = graphCache.getGraph(building, level)
        if len(floorGraph.edges) == 0:
            raise Exception("Looks like there is no such location. Try again")

        confirmation = False
        while not confirmation:
            EarphonesApi.outputText("Please specify Location")
            location = KeyPadApi.getLocation(floorGraph.getNodes())
            EarphonesApi.outputText("You have input " + location.getName() + ". Is this correct?")
            confirmation = KeyPadApi.getConfirmation()

        point = floorGraph.pointsIdMap.get(floorGraph.nodeNameIdMap.get(location.getName()))
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