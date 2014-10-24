import time
from business.cache.GraphCache import GraphCache
from business.deadreckoning.DirectionSpecifier import DirectionSpecifier
from business.deadreckoning.PositionCalculator import PositionCalculator
from business.graph.dijkstra.PathRetriever import PathRetriever
from business.graph.location.LocationRetriever import LocationRetriever
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


#This is where the execution begins

#Check if internet access is available first.
while not internet_on():
    time.sleep(5)
    EarphonesApi.outputText("No access to the network yet. Sleeping for 5 seconds.")

initialMessage()
performHandshake()
initialPosition = getInitialPosition()
destination = getDestination()

graphCache = GraphCache()
floorGraph = graphCache.getGraph(initialPosition.getBuilding(), initialPosition.getLevel())

shortestPathNodes = PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(), destination.getName())

#initialize the singleton here
positionCalculator = PositionCalculator(initialPosition.getX(), initialPosition.getY(), floorGraph.northAt)


from business.deadreckoning.SerialQueueListener import SerialQueueListener

nextSteps = DirectionSpecifier()
nextSteps.setLocationQueue(shortestPathNodes)
print nextSteps.locationQueue

integrationSerial.sendMessage('1')

t = Thread(target=SerialQueueListener.listen)
t.daemon = True
t.start()
time.sleep(0.5)

positionCalculator.directionSpecifier.next(initialPosition.getX(), initialPosition.getY(),
                                           positionCalculator.getCurrentDirection(), floorGraph.northAt)



wifiThread = Thread(target=WiFiPoller.poll)
wifiThread.daemon = True
wifiThread.start()

t = Thread(target=clientSerial.run)
t.start()
