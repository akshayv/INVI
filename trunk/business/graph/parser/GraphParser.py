from domain.graph.Edge import Edge
from domain.graph.ListGraph import ListGraph
from domain.graph.Point import Point
from integration.http.map.MapRetriever import MapRetriever

__author__ = 'akshay'


class GraphParser:

    @staticmethod
    def parseGraph(graphJson, building = "", level = 2):
        northAt = float(graphJson["info"]["northAt"])
        graphJson = graphJson["map"]
        listGraph = ListGraph(len(graphJson), northAt)
        for point in graphJson:
            offset = 0.0
            if (building == "2" or building == "COM2") and (level == "2" or level == 2):
                offset = 15.0
                if point["nodeName"] == "P17" or point["nodeName"] == "P2" or point["nodeName"] == "P5" or point[
                    "nodeName"] == "P19":
                    offset = 25.0
            pointObject = Point(int(point["nodeId"]) - 1, float(point["x"]), float(point["y"]),
                                point["nodeName"], offset)
            for linkedPointId in point["linkTo"].split(","):
                # Map from 1-9 to 0-8
                modifiedLinkedPointId = int(linkedPointId) - 1
                linkedPoint = graphJson[modifiedLinkedPointId]

                offset = 0.0
                if (building == "2" or building == "COM2") and (level == "2" or level == 2):
                    offset = 15.0
                    if linkedPoint["nodeName"] == "P17" or linkedPoint["nodeName"] == "P2" or linkedPoint[
                        "nodeName"] == "P5" or linkedPoint["nodeName"] == "P19":
                        offset = 25.0
                linkedPointObject = Point(modifiedLinkedPointId, float(linkedPoint["x"]), float(linkedPoint["y"]),
                                          linkedPoint["nodeName"], offset)

                # The sample data was buggy. This is an unnecessary check
                if not listGraph.isEdge(pointObject.getId(), linkedPointObject.getId()):
                    listGraph.insert(
                        Edge(pointObject,
                             linkedPointObject, Edge.getDistanceBetweenPoints(pointObject, linkedPointObject)))
        return listGraph


if __name__ == "__main__":
    graphParser = GraphParser()
    graphJson = MapRetriever().retrieveData(2, 2)
    listGraph = graphParser.parseGraph(graphJson)
    print listGraph