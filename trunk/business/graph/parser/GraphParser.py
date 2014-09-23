from domain.graph.Edge import Edge
from domain.graph.ListGraph import ListGraph
from domain.graph.Point import Point
from integration.http.map.MapRetriever import MapRetriever

__author__ = 'akshay'


class GraphParser:

    @staticmethod
    def parseGraph(graphJson):
        northAt = float(graphJson["info"]["northAt"])
        graphJson = graphJson["map"]
        listGraph = ListGraph(len(graphJson), northAt)
        for point in graphJson:
            pointObject = Point(int(point["nodeId"]) - 1, float(point["x"]), float(point["y"]), point["nodeName"])
            for linkedPointId in point["linkTo"].split(","):
                # Map from 1-9 to 0-8
                modifiedLinkedPointId = int(linkedPointId) - 1
                linkedPoint = graphJson[modifiedLinkedPointId]

                linkedPointObject = Point(modifiedLinkedPointId, float(linkedPoint["x"]), float(linkedPoint["y"]),
                                          linkedPoint["nodeName"])

                # The sample data was buggy. This is an unnecessary check
                if not listGraph.isEdge(pointObject.getId(), linkedPointObject.getId()):
                    listGraph.insert(
                        Edge(pointObject,
                             linkedPointObject, Edge.getDistanceBetweenPoints(pointObject, linkedPointObject)))
        return listGraph


if __name__ == "__main__":
    graphParser = GraphParser()
    graphJson = MapRetriever().retrieveData("DemoBuilding", 1)
    listGraph = graphParser.parseGraph(graphJson)
    print listGraph