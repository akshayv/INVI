import json
from business.graph.parser.GraphParser import GraphParser
from integration.http.map.MapRetriever import MapRetriever

__author__ = 'akshay'


class GraphCache(object):

    __graphCache = {}
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(GraphCache, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        com1level2 = self.getGraph("1", "2")
        com2level2 = self.getGraph("2", "2")
        com2level3 = self.getGraph("2", "3")
        self.__graphCache["1-L2"] = com1level2
        self.__graphCache["2-L2"] = com2level2
        self.__graphCache["2-L3"] = com2level3
        self.__graphCache["COM1-L2"] = com1level2
        self.__graphCache["COM2-L2"] = com2level2
        self.__graphCache["COM2-L3"] = com2level3

    def getGraph(self, building, level):
        key = building + "-L" + level
        if not key in GraphCache.__graphCache:
            graph = GraphParser.parseGraph(MapRetriever.retrieveData(building, level))
            GraphCache.__graphCache[key] = graph
        return GraphCache.__graphCache.get(building + "-L" + level)
