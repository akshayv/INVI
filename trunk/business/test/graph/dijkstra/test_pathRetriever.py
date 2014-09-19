from unittest import TestCase
from business.graph.dijkstra.PathRetriever import PathRetriever
from business.graph.parser.GraphParser import GraphParser
from integration.http.map.MapRetriever import MapRetriever

__author__ = 'akshay'


class TestPathRetriever(TestCase):
    def test_getShortestPath(self):
        listGraph = GraphParser.parseGraph(MapRetriever().retrieveData("COM1", 2))
        self.assertEqual(str(PathRetriever.getShortestPath(listGraph, "Linkway", "Seminar Room 2")), '[2, 1, 3, 4, 7, 8]')