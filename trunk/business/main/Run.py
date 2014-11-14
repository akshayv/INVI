from business.cache.GraphCache import GraphCache
from business.graph.dijkstra.PathRetriever import PathRetriever
from domain.graph.Position import Position

__author__ = 'akshay'


def getShortestPathNodes(initialPosition, destination):

    graphCache = GraphCache()
    shortestPathNodes = []
    floorGraph = graphCache.getGraph(initialPosition.getBuilding(), initialPosition.getLevel())
    if destination.getBuilding() is not initialPosition.getBuilding() or destination.getLevel() is not initialPosition.getLevel():
        if initialPosition.getBuilding() == "1" or initialPosition.getBuilding() == "COM1":
            if destination.getLevel() == "2":
                shortestPathNodes.append({"graph":
                                              PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(),
                                                                                 "TO 2-2-1"),
                                          "northAt": floorGraph.northAt})

                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), destination.getLevel()), "TO 1-2-31",
                    destination.getName()),
                                          "northAt": graphCache.getGraph(destination.getBuilding(),
                                                                         destination.getLevel()).northAt})

            elif destination.getLevel() == "3":
                shortestPathNodes.append({"graph":
                    PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(), "TO 2-2-1"),
                                          "northAt": floorGraph.northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), "2"), "TO 1-2-31",
                    "TO 2-3-12"), "northAt": graphCache.getGraph(destination.getBuilding(), "2").northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), "3"), "TO 2-2-16",
                    destination.getName()), "northAt": graphCache.getGraph(destination.getBuilding(), "3").northAt})

        elif (
                    initialPosition.getBuilding() == "2" or initialPosition.getBuilding() == "COM2") and initialPosition.getLevel() == "2":
            if destination.getBuilding() == "1":
                shortestPathNodes.append({"graph":
                    PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(), "TO 1-2-31"),
                                          "northAt": floorGraph.northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), destination.getLevel()), "TO 2-2-1",
                    destination.getName()), "northAt": graphCache.getGraph(destination.getBuilding(),
                                                                           destination.getLevel()).northAt})

            elif destination.getLevel() == "3":
                shortestPathNodes.append({"graph":
                                              PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(),
                                                                                 "TO 2-3-12"),
                                          "northAt": floorGraph.northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), destination.getLevel()), "TO 2-2-16",
                    destination.getName()), "northAt": graphCache.getGraph(destination.getBuilding(),
                                                                           destination.getLevel()).northAt})

        elif (
                    initialPosition.getBuilding() == "2" or initialPosition.getBuilding() == "COM2") and initialPosition.getLevel() == "3":
            if destination.getBuilding() == "1":
                shortestPathNodes.append({"graph":
                                              PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(),
                                                                                 "TO 2-2-16"),
                                          "northAt": floorGraph.northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(initialPosition.getBuilding(), "2"), "TO 2-3-12",
                    "TO 1-2-31"), "northAt": graphCache.getGraph(initialPosition.getBuilding(), "2").northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), destination.getLevel()), "TO 2-2-1",
                    destination.getName()), "northAt": graphCache.getGraph(destination.getBuilding(),
                                                                           destination.getLevel()).northAt})
            elif destination.getLevel() == "2":
                shortestPathNodes.append({"graph":
                                              PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(),
                                                                                 "TO 2-2-16"),
                                          "northAt": floorGraph.northAt})
                shortestPathNodes.append({"graph": PathRetriever.getShortestPathNodes(
                    graphCache.getGraph(destination.getBuilding(), destination.getLevel()), "TO 2-3-12",
                    destination.getName()), "northAt": graphCache.getGraph(destination.getBuilding(),
                                                                           destination.getLevel()).northAt})

    else:
        shortestPathNodes.append({"graph":
                                      PathRetriever.getShortestPathNodes(floorGraph, initialPosition.getName(),
                                                                         destination.getName()),
                                  "northAt": floorGraph.northAt})
    return shortestPathNodes


initialPosition = Position("2", "2", 121.0, 252.2, "P2")
destination = Position("2", "2", 121.0, 252.2, "Stairwell")
shortestPathNodes = getShortestPathNodes(initialPosition, destination)
print(shortestPathNodes)
