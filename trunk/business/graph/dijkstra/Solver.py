from business.graph.parser.GraphParser import GraphParser
from business.graph.parser import GraphParser as gp
from domain.graph.ListGraph import ListGraph
from domain.graph import ListGraph as lg

__author__ = 'akshay'


class Solver:

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
                v = edge.getDestNodeId()
                if vMinusS.__contains__(v):
                    distance = edge.getDistance()
                    if dist[u] + distance < dist[v]:
                        dist[v] = dist[u] + distance
                        pred[v] = u


if __name__ == "__main__":
    listGraph = lg.getDefaultGraph()
    pred = [None] * listGraph.numV
    dist = [None] * listGraph.numV
    Solver.solveGraph(listGraph, 3, pred, dist)
    print pred
    print dist
    print
    print
    listGraph = GraphParser.parseGraph(gp.getDefaultJson())
    pred = [None] * listGraph.numV
    dist = [None] * listGraph.numV
    Solver.solveGraph(listGraph, 7, pred, dist)
    print pred
    print dist