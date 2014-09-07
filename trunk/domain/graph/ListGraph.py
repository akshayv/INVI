from domain.graph.Edge import Edge

__author__ = 'akshay'


class ListGraph:
    edges = None
    numV = 0

    def __init__(self, numV):
        self.numV = numV
        self.edges = []
        for i in range(0, numV):
            self.edges.append([])

    def getConnectedEdges(self, edge):
        return self.edges[edge]

    def getEdge(self, source, dest):
        target = Edge(source, dest, float("inf"))
        for edge in self.edges[source]:
            if edge.__eq__(target):
                return edge
        return target

    def isEdge(self, source, dest):
        edges = self.edges[source]
        currEdge = Edge(source, dest, 1)
        if currEdge in edges:
            return True
        return False

    def insert(self, edge):
        self.edges[edge.getSourceNodeId()].append(edge)
        self.edges[edge.getDestNodeId()].append(Edge(edge.getDestNodeId(),
                                                  edge.getSourceNodeId(),
                                                  edge.getDistance()))

    def __str__(self):
        string = ""
        for i in range(0, len(self.edges)):
            lcl_edges = self.edges[i]
            for j in range(0, len(lcl_edges)):
                string += " " + str(lcl_edges[j]) + " "
            string += "\n"
        return string


def getDefaultGraph():
    listGraph = ListGraph(10)
    edge = Edge(0, 1, 5)
    listGraph.insert(edge)
    edge = Edge(1, 2, 4)
    listGraph.insert(edge)
    edge = Edge(2, 3, 3)
    listGraph.insert(edge)
    edge = Edge(2, 4, 2)
    listGraph.insert(edge)
    edge = Edge(4, 5, 1)
    listGraph.insert(edge)
    edge = Edge(4, 6, 9)
    listGraph.insert(edge)
    edge = Edge(4, 7, 2)
    listGraph.insert(edge)
    edge = Edge(7, 8, 4)
    listGraph.insert(edge)
    edge = Edge(8, 9, 5)
    listGraph.insert(edge)
    return listGraph


if __name__ == "__main__":
    listGraph = getDefaultGraph()
    print listGraph
    print listGraph.getEdge(2, 3)
    print listGraph.isEdge(2, 4)
