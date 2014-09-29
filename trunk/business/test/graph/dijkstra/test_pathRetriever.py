from unittest import TestCase
from business.graph.dijkstra.PathRetriever import PathRetriever
from business.graph.parser.GraphParser import GraphParser
from integration.http.map.MapRetriever import MapRetriever

__author__ = 'akshay'


class TestPathRetriever(TestCase):
    def test_getShortestPath(self):
        listGraph = GraphParser.parseGraph(MapRetriever.retrieveData("COM1", 2))
        self.assertEqual(str(PathRetriever.getShortestPath(listGraph, "Linkway", "Seminar Room 2")),
                         '[2, 1, 3, 4, 7, 8]')


    def test_getShortestPath_Nodes1(self):
        listGraph = GraphParser.parseGraph(MapRetriever.retrieveData("DemoBuilding", 2))
        self.assertEqual(str(PathRetriever.getShortestPathNodes(listGraph, "Some more Corridor", "TO level 1,3")),
                         '[( nodeId = 3, x = 400.0, y = 100.0, name = Some more Corridor ), ( nodeId = 2, x = 600.0, y = 100.0, name = Still Corridor ), ( nodeId = 1, x = 800.0, y = 100.0, name = Corridor ), ( nodeId = 0, x = 800.0, y = 300.0, name = TO level 1,3 )]')

    def test_getShortestPath_Nodes2(self):
        listGraph = GraphParser.parseGraph(MapRetriever.retrieveData("COM1", 2))
        self.assertEqual(str(PathRetriever.getShortestPathNodes(listGraph, "P4", "P17")),
                         '[( nodeId = 3, x = 1420.0, y = 1260.0, name = P4 ), ( nodeId = 6, x = 1860.0, y = 1260.0, name = lobby  ), ( nodeId = 9, x = 1860.0, y = 780.0, name = P10 ), ( nodeId = 10, x = 2760.0, y = 780.0, name = Student Area ), ( nodeId = 13, x = 3480.0, y = 780.0, name = P14 ), ( nodeId = 14, x = 3480.0, y = 1380.0, name = P15 ), ( nodeId = 16, x = 4440.0, y = 1380.0, name = P17 )]')

    def test_getShortestPath_Nodes3(self):
        listGraph = GraphParser.parseGraph(MapRetriever.retrieveData("COM1", 2))
        self.assertEqual(str(PathRetriever.getShortestPathNodes(listGraph, "Seminar Room 1", "Tutorial Room 9")),
                         '[( nodeId = 11, x = 2760.0, y = 1440.0, name = Seminar Room 1 ), ( nodeId = 10, x = 2760.0, y = 780.0, name = Student Area ), ( nodeId = 13, x = 3480.0, y = 780.0, name = P14 ), ( nodeId = 15, x = 3480.0, y = 360.0, name = P16 ), ( nodeId = 17, x = 4080.0, y = 360.0, name = P18 ), ( nodeId = 21, x = 4800.0, y = 360.0, name = P22 ), ( nodeId = 24, x = 4800.0, y = 520.0, name = Tutorial Room 9 )]')