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

    def getGraph(self, building, level):
        key = building + "-L" + level
        if not key in GraphCache.__graphCache:
            graph = GraphParser.parseGraph(MapRetriever.retrieveData(building, level))
            GraphCache.__graphCache[key] = graph
        return GraphCache.__graphCache.get(building + "-L" + level)