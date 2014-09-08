from business.graph.dijkstra.Solver import Solver
from business.graph.parser.GraphParser import GraphParser
from business.graph.parser import GraphParser as gp

__author__ = 'akshay'

class PathRetriever:

    @staticmethod
    def getShortestPath(graph, sourceNodeName, destNodeName):
        if sourceNodeName not in graph.nodeNameIdMap or destNodeName not in graph.nodeNameIdMap :
            raise Exception("No such source node or destination node. Please fix this")
        sourceNodeId = graph.nodeNameIdMap[sourceNodeName]
        destNodeId = graph.nodeNameIdMap[destNodeName]

        parent = [None] * graph.numV
        distance = [None] * graph.numV

        Solver.solveGraph(graph, sourceNodeId, parent, distance)

        shortestPath = [destNodeId]

        prev = parent[destNodeId]
        while prev is not None:
            shortestPath.append(prev)
            prev = parent[prev]

        shortestPath.reverse()
        return shortestPath

if __name__ == "__main__":
    listGraph = GraphParser.parseGraph(gp.getDefaultJson())
    print PathRetriever.getShortestPath(listGraph, "Entrance", "TO level 2")