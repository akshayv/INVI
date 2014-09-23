from business.cache.GraphCache import GraphCache
from business.graph.parser.VoiceParser import VoiceParser
from domain.graph.Position import Position
from integration.earphones.EarphonesApi import EarphonesApi
from integration.microphone.MicrophoneApi import MicrophoneApi

__author__ = 'akshay'


class PositionRetriever:

    @staticmethod
    def getPosition():

        EarphonesApi.outputText("Please specify Building Name")
        building = MicrophoneApi.getUserInput()

        EarphonesApi.outputText("Please specify Level")
        level = MicrophoneApi.getUserInput()

        EarphonesApi.outputText("Retrieving graph now.")
        graphCache = GraphCache()
        floorGraph = graphCache.getGraph(building, level)
        if len(floorGraph.edges) == 0:
            raise Exception("Looks like there is no such location. Try again")

        EarphonesApi.outputText("Please specify Location Name")
        location = "Semilar Rom 11"

        locationString = VoiceParser.getMatchingLocation(location, floorGraph.nodeNameIdMap.keys())
        point = floorGraph.pointsIdMap.get(floorGraph.nodeNameIdMap.get(locationString))
        position = Position(building, level, point.getX(), point.getY(), point.getName())
        return position


    @staticmethod
    def getInitialPosition():
        EarphonesApi.outputText("Please specify initial position")
        return PositionRetriever.getPosition()

    @staticmethod
    def getDestination():
        EarphonesApi.outputText("Please specify destination")
        return PositionRetriever.getPosition()


if __name__ == "__main__":
    PositionRetriever.getInitialPosition()