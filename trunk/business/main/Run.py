from business.cache.GraphCache import GraphCache
from business.deadreckoning.DirectionSpecifier import DirectionSpecifier
from business.deadreckoning.PositionCalculator import PositionCalculator
from business.deadreckoning.SerialQueueListener import SerialQueueListener
from business.graph.dijkstra.PathRetriever import PathRetriever
from business.graph.location.LocationRetriever import LocationRetriever
from business.wifi.WiFiPoller import WiFiPoller
from clientapis.serial.SerialCommApi import SerialCommApi
from integration.earphones.EarphonesApi import EarphonesApi

__author__ = 'akshay'

from threading import Thread


def getShortestPath():
    shortestPath = PathRetriever.getShortestPath(floorGraph, initialPosition.getName(), destination.getName())
    shortestPathNodes = []
    for iterator in range(0, len(shortestPath)):
        shortestPathNodes.append(floorGraph.pointsIdMap[shortestPath[iterator]])
    return shortestPathNodes


def getInitialPosition():
    initialPosition = None
    while True:
        try:
            initialPosition = LocationRetriever.getInitialLocation()
            break
        except Exception as e:
            EarphonesApi.outputText(e.message)
            continue
    return initialPosition


def getDestination():
    destination = None
    while True:
        try:
            destination = LocationRetriever.getDestination()
            break
        except Exception as e:
            EarphonesApi.outputText(e.message)
            continue
    return destination


def initialMessage():
    EarphonesApi.outputText("System is online.")

#This is where the execution begins

initialMessage()
initialPosition = getInitialPosition()
destination = getDestination()

graphCache = GraphCache()
floorGraph = graphCache.getGraph(initialPosition.getBuilding(), initialPosition.getLevel())

shortestPathNodes = PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(), destination.getName())

#initialize the singleton here
positionCalculator = PositionCalculator(initialPosition.getX(), initialPosition.getY(), floorGraph.northAt)

nextSteps = DirectionSpecifier()
nextSteps.setLocationQueue(shortestPathNodes)
print nextSteps.locationQueue

EarphonesApi.outputText("Please take a step forward")


t = Thread(target=SerialQueueListener.listen)
t.daemon = True
t.start()

wifiThread = Thread(target=WiFiPoller.poll)
wifiThread.daemon = True
wifiThread.start()


t = Thread(target=SerialCommApi.run)
t.start()