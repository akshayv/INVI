from unittest import TestCase
from business.graph.parser.GraphParser import GraphParser
from domain.graph import ListGraph as lg
from business.graph.dijkstra.DijkstraSolver import DijkstraSolver
from integration.http.map.MapRetriever import MapRetriever

__author__ = 'akshay'


class TestDijkstraSolver(TestCase):
    def test_solveGraph(self):
        listGraph = lg.getDefaultGraph()
        pred = [None] * listGraph.numV
        dist = [None] * listGraph.numV
        DijkstraSolver.solveGraph(listGraph, 3, pred, dist)
        self.assertEqual(str(pred), '[1, 2, 3, None, 2, 4, 4, 4, 7, 8]')
        self.assertEqual(str(dist), '[12, 7, 3, None, 5, 6, 14, 7, 11, 16]')

        listGraph = GraphParser.parseGraph(MapRetriever().retrieveData("DemoBuilding", 1))
        pred = [None] * listGraph.numV
        dist = [None] * listGraph.numV
        DijkstraSolver.solveGraph(listGraph, 7, pred, dist)
        self.assertEqual(str(pred), '[1, 2, 7, 2, 7, 4, 5, None]')
        self.assertEqual(str(dist), '[600.0, 400.0, 300.0, 500.0, 200.0, 400.0, 600.0, None]')

    def test_solveGraph2(self):
        listGraph = GraphParser.parseGraph(MapRetriever().retrieveData("COM1", 2))
        pred = [None] * listGraph.numV
        dist = [None] * listGraph.numV
        DijkstraSolver.solveGraph(listGraph, 3, pred, dist)
        self.assertEqual(str(pred), '[1, 3, 1, None, 3, 3, 3, 4, 7, 6, 9, 10, 10, 10, 13, 13, 14, 15, 16, 17, 16, 17, 20, 20, 21, 21, 23, 25, 25, 27, 28]')
        self.assertEqual(str(dist), '[1420.0, 360.0, 1260.0, None, 480.0, 180.0, 440.0, 700.0, 1020.0, 920.0, 1820.0, 2480.0, 2240.0, 2540.0, 3140.0, 2960.0, 4100.0, 3560.0, 4400.0, 3720.0, 4320.0, 4280.0, 4540.0, 4880.0, 4440.0, 4700.0, 5100.0, 4960.0, 5180.0, 5782.192191643779, 5336.204993518133]')

    def test_solveGraph3(self):
        listGraph = GraphParser.parseGraph(MapRetriever().retrieveData("DemoBuilding", 2))
        pred = [None] * listGraph.numV
        dist = [None] * listGraph.numV
        DijkstraSolver.solveGraph(listGraph, 2, pred, dist)
        self.assertEqual(str(pred), '[1, 2, None, 2, 3]')
        self.assertEqual(str(dist), '[400.0, 200.0, None, 200.0, 400.0]')
