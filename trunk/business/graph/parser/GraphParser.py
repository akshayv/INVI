import json
from domain.graph.Edge import Edge
from domain.graph.ListGraph import ListGraph
from domain.graph.Point import Point

__author__ = 'akshay'


class GraphParser:
    @staticmethod
    def parseGraph(graphJsonAsString):
        graphJson = json.loads(graphJsonAsString)
        listGraph = ListGraph(len(graphJson))
        for point in graphJson:
            pointObject = Point(int(point["nodeId"]) - 1, float(point["x"]), float(point["y"]), point["nodeName"])
            for linkedPointId in point["linkTo"].split(", "):
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


def getDefaultJson():
    return '[{"nodeId": "1", "x": "200", "y": "100", "nodeName": "Entrance", "linkTo": "2"},{"nodeId": "2", "x": "400", "y": "100", "nodeName": "Room 1", "linkTo": "3"},{"nodeId": "3", "x": "400", "y": "200", "nodeName": "Room 2", "linkTo": "4, 8"},{"nodeId": "4", "x": "600", "y": "200", "nodeName": "Male Toilet", "linkTo": "6"},{"nodeId": "5", "x": "600", "y": "500", "nodeName": "Female Toilet", "linkTo": "8, 6"}, {"nodeId": "6", "x": "600", "y": "300", "nodeName": "Corridor", "linkTo": "4, 5, 7"}, {"nodeId": "7", "x": "800", "y": "300", "nodeName": "TO level 2", "linkTo": "6"}, {"nodeId": "8", "x": "400", "y": "500", "nodeName": "Room 3", "linkTo": "3, 5"}]'


if __name__ == "__main__":
    graphParser = GraphParser()
    graphJson = getDefaultJson()
    listGraph = graphParser.parseGraph(graphJson)
    print listGraph