from business.cache.GraphCache import GraphCache
from business.deadreckoning.SerialQueueListener import SerialQueueListener
from business.graph.dijkstra.PathRetriever import PathRetriever
from business.graph.position.PositionRetriever import PositionRetriever

__author__ = 'akshay'

from threading import Thread


initialPosition = PositionRetriever.getInitialPosition()

destination = PositionRetriever.getDestination()

graphCache = GraphCache()
floorGraph = graphCache.getGraph(initialPosition.getBuilding(), initialPosition.getLevel())

shortestPath = PathRetriever.getShortestPath(floorGraph, initialPosition.getName(), destination.getName())

print shortestPath

t = Thread(target=SerialQueueListener.listen)
t.daemon = True
t.start()
#
# wifiThread = Thread(Wifi.poll)
# wifiThread.daemon = True
# wifiThread.start()

