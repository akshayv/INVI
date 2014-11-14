import time
from business.cache.GraphCache import GraphCache
from business.deadreckoning.DirectionSpecifier import DirectionSpecifier
from business.deadreckoning.NorthAt import NorthAt
from business.deadreckoning.PositionCalculator import PositionCalculator
from business.graph.dijkstra.PathRetriever import PathRetriever
from business.graph.location.LocationRetriever import LocationRetriever
from domain.deadreckoning.SensorReading import SensorReading
from integration.earphones.EarphonesApi import EarphonesApi
from integration.serial.SerialCommApi import SerialCommApi as integrationSerial
from clientapis.serial.SerialCommApi import SerialCommApi as clientSerial
from business.wifi.WiFiPoller import WiFiPoller
import urllib2

__author__ = 'akshay'

from threading import Thread


def internet_on():
    try:
        urllib2.urlopen('http://showmyway.comp.nus.edu.sg', timeout=1)
        return True
    except urllib2.URLError as err:
        pass
    return False


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


def performHandshake():
    EarphonesApi.outputText("Performing handshake now.")
    print "Performing handshake"
    isHandShakeSuccessful = False
    while not isHandShakeSuccessful:
        EarphonesApi.outputText("Looping handshake")
        integrationSerial.sendMessage('1')
        print "Sent"
        message = clientSerial.getMessage()
        print "Incoming message was:" + str(message)
        if message is not '':
            print "Send and receive successful"
            integrationSerial.sendMessage('1')
            isHandShakeSuccessful = True
        time.sleep(3)

def getShortestPathNodes(initialPosition, destination):

    graphCache = GraphCache()
    shortestPathNodes = []
    floorGraph = graphCache.getGraph(initialPosition.getBuilding(), initialPosition.getLevel())
    if destination.getBuilding() is not initialPosition.getBuilding() or destination.getLevel() is not initialPosition.getLevel():
        if initialPosition.getBuilding() == "1" or initialPosition.getBuilding() == "COM1":
            if destination.getLevel() == "2":
                shortestPathNodes.append({"graph":
                                              PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(),
                                                                                 "TO 2-2-1"),
                                          "northAt": floorGraph.northAt})

                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), destination.getLevel()), "TO 1-2-31",
                    destination.getName()),
                                          "northAt": graphCache.getGraph(destination.getBuilding(),
                                                                         destination.getLevel()).northAt})

            elif destination.getLevel() == "3":
                shortestPathNodes.append({"graph":
                    PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(), "TO 2-2-1"),
                                          "northAt": floorGraph.northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), "2"), "TO 1-2-31",
                    "TO 2-3-12"), "northAt": graphCache.getGraph(destination.getBuilding(), "2").northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), "3"), "TO 2-2-16",
                    destination.getName()), "northAt": graphCache.getGraph(destination.getBuilding(), "3").northAt})

        elif (
                    initialPosition.getBuilding() == "2" or initialPosition.getBuilding() == "COM2") and initialPosition.getLevel() == "2":
            if destination.getBuilding() == "1":
                shortestPathNodes.append({"graph":
                    PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(), "TO 1-2-31"),
                                          "northAt": floorGraph.northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), destination.getLevel()), "TO 2-2-1",
                    destination.getName()), "northAt": graphCache.getGraph(destination.getBuilding(),
                                                                           destination.getLevel()).northAt})

            elif destination.getLevel() == "3":
                shortestPathNodes.append({"graph":
                                              PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(),
                                                                                 "TO 2-3-12"),
                                          "northAt": floorGraph.northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), destination.getLevel()), "TO 2-2-16",
                    destination.getName()), "northAt": graphCache.getGraph(destination.getBuilding(),
                                                                           destination.getLevel()).northAt})

        elif (
                    initialPosition.getBuilding() == "2" or initialPosition.getBuilding() == "COM2") and initialPosition.getLevel() == "3":
            if destination.getBuilding() == "1":
                shortestPathNodes.append({"graph":
                                              PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(),
                                                                                 "TO 2-2-16"),
                                          "northAt": floorGraph.northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(initialPosition.getBuilding(), "2"), "TO 2-3-12",
                    "TO 1-2-31"), "northAt": graphCache.getGraph(initialPosition.getBuilding(), "2").northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), destination.getLevel()), "TO 2-2-1",
                    destination.getName()), "northAt": graphCache.getGraph(destination.getBuilding(),
                                                                           destination.getLevel()).northAt})
            elif destination.getLevel() == "2":
                shortestPathNodes.append({"graph":
                                              PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(),
                                                                                 "TO 2-2-16"),
                                          "northAt": floorGraph.northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), destination.getLevel()), "TO 2-3-12",
                    destination.getName()), "northAt": graphCache.getGraph(destination.getBuilding(),
                                                                           destination.getLevel()).northAt})

    else:
        shortestPathNodes.append({"graph":
                                      PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(),
                                                                         destination.getName()),
                                  "northAt": floorGraph.northAt})
    return shortestPathNodes


# This is not really a good way to do things but it is a quick fix
def getInitialDirection():
    compassVal = None
    while compassVal is None:
        try:
            EarphonesApi.outputText("Trying to get compass direction")
            inp = clientSerial.serial.readline()
            compassVal = SensorReading.fromString(inp).compassReading
            EarphonesApi.outputText("Got initial compass direction")
        except Exception:
            print "ERROR DATA"
    positionCalculator.directionSpecifier.next(initialPosition.getX(), initialPosition.getY(), compassVal)

#This is where the execution begins

#Check if internet access is available first.
while not internet_on():
    time.sleep(5)
    EarphonesApi.outputText("No access to the network yet. Sleeping for 5 seconds.")

initialMessage()
performHandshake()
initialPosition = getInitialPosition()
destination = getDestination()

shortestPathNodes = getShortestPathNodes(initialPosition, destination)

floorGraph = GraphCache().getGraph(initialPosition.getBuilding(), initialPosition.getLevel())

#initialize the singleton here
positionCalculator = PositionCalculator(initialPosition.getX(), initialPosition.getY())

from business.deadreckoning.SerialQueueListener import SerialQueueListener

nextSteps = DirectionSpecifier()
nextSteps.setLocationQueue(shortestPathNodes)
print nextSteps.locationQueue

t = Thread(target=SerialQueueListener.listen)
t.daemon = True
t.start()

wifiThread = Thread(target=WiFiPoller.poll)
wifiThread.daemon = True
wifiThread.start()

integrationSerial.sendMessage('1')
integrationSerial.sendMessage('1')

getInitialDirection()

t = Thread(target=clientSerial.run)
t.start()
