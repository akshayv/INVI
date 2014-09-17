from unittest import TestCase
from business.graph.dijkstra.PathRetriever import PathRetriever
from business.graph.parser.GraphParser import GraphParser
from integration.http.map.MapRetriever import MapRetriever

__author__ = 'akshay'


class TestPathRetriever(TestCase):
    def test_getShortestPath(self):
        listGraph = GraphParser.parseGraph(MapRetriever().retrieveData("DemoBuilding", 1))
        self.assertEqual(str(PathRetriever.getShortestPath(listGraph, "Entrance", "TO level 2")), '[0, 1, 2, 3, 5, 6]')