from domain.graph.Edge import Edge
from domain.graph.Point import Point

__author__ = 'akshay'


class ListGraph:
    edges = None
    numV = 0
    nodeNameIdMap = {}

    def __init__(self, numV):
        self.numV = numV
        self.edges = []
        for i in range(0, numV):
            self.edges.append([])

    def getConnectedEdges(self, edge):
        return self.edges[edge]

    def getEdge(self, source, dest):
        target = Edge(Point(source), Point(dest), float("inf"))
        for edge in self.edges[source]:
            if edge.__eq__(target):
                return edge
        return target

    def isEdge(self, source, dest):
        edges = self.edges[source]
        currEdge = Edge(Point(source), Point(dest), 1)
        if currEdge in edges:
            return True
        return False

    def insert(self, edge):
        if edge.getSourceNode().getName() not in self.nodeNameIdMap:
            self.nodeNameIdMap[edge.getSourceNode().getName()] = edge.getSourceNode().getId()

        if edge.getDestNode().getName() not in self.nodeNameIdMap:
            self.nodeNameIdMap[edge.getDestNode().getName()] = edge.getDestNode().getId()

        self.edges[edge.getSourceNode().getId()].append(edge)
        self.edges[edge.getDestNode().getId()].append(Edge(edge.getDestNode(),
                                                     edge.getSourceNode(),
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
    point0 = Point(0, 0, 0, "Point0")
    point1 = Point(1, 0, 0, "Point1")
    point2 = Point(2, 0, 0, "Point2")
    point3 = Point(3, 0, 0, "Point3")
    point4 = Point(4, 0, 0, "Point4")
    point5 = Point(5, 0, 0, "Point5")
    point6 = Point(6, 0, 0, "Point6")
    point7 = Point(7, 0, 0, "Point7")
    point8 = Point(8, 0, 0, "Point8")
    point9 = Point(9, 0, 0, "Point9")
    edge = Edge(point0, point1, 5)
    listGraph.insert(edge)
    edge = Edge(point1, point2, 4)
    listGraph.insert(edge)
    edge = Edge(point2, point3, 3)
    listGraph.insert(edge)
    edge = Edge(point2, point4, 2)
    listGraph.insert(edge)
    edge = Edge(point4, point5, 1)
    listGraph.insert(edge)
    edge = Edge(point4, point6, 9)
    listGraph.insert(edge)
    edge = Edge(point4, point7, 2)
    listGraph.insert(edge)
    edge = Edge(point7, point8, 4)
    listGraph.insert(edge)
    edge = Edge(point8, point9, 5)
    listGraph.insert(edge)
    return listGraph


if __name__ == "__main__":
    listGraph = getDefaultGraph()
    print listGraph
    print listGraph.getEdge(2, 3)
    print listGraph.isEdge(2, 4)
