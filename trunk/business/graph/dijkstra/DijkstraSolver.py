from business.graph.parser.GraphParser import GraphParser
from domain.graph.ListGraph import ListGraph
from domain.graph import ListGraph as lg
from integration.http.map.MapRetriever import MapRetriever

__author__ = 'akshay'


class DijkstraSolver:

    @staticmethod
    def solveGraph(graph, start, pred, dist):

        if not isinstance(graph, ListGraph):
            raise Exception("Cannot solve the graph if it is not of type ListGraph")

        numV = graph.numV
        vMinusS = set()
        for i in range(0, numV):
            if i != start:
                vMinusS.add(i)

        for v in vMinusS:
            pred[v] = start
            dist[v] = graph.getEdge(start, v).getDistance()

        while len(vMinusS) != 0:
            #TODO: Have a Priority Queue implementation
            minDist = float("inf")
            u = -1
            for v in vMinusS:
                if dist[v] < minDist:
                    minDist = dist[v]
                    u = v
            vMinusS.remove(u)
            for edge in graph.getConnectedEdges(u):
                v = edge.getDestNode().getId()
                if vMinusS.__contains__(v):
                    distance = edge.getDistance()
                    if dist[u] + distance < dist[v]:
                        dist[v] = dist[u] + distance
                        pred[v] = u