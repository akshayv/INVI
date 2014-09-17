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