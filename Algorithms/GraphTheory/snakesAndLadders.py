#!/bin/python3

import sys

def quickestWayUp(mapping):
    # Complete this function
    adjacencyList = createAdjacencyList(mapping)
    return getShortestPath(adjacencyList)

def createAdjacencyList(mapping):
    adjacencyList = [[] for i in range(101)]
    for startPoint in range(1, 101):
        if startPoint in mapping:
            continue
        neighbors = []
        for numberOfPlacesMoved in range(1, 7):
            endPoint = startPoint + numberOfPlacesMoved
            if endPoint in mapping:
                endPoint = mapping[endPoint] #swap for other destination
            if endPoint > 100:
                continue
            neighbors.append(endPoint)
        adjacencyList[startPoint] = neighbors
    return adjacencyList

    
def getShortestPath(adjacencyList):
    queue = set( {1} )
    distances = [float("inf") if i != 1 else 0 for i in range(101)]
    seen = [False for i in range(101)]
    while len(queue) > 0:
        square = min(queue, key = lambda square : distances[square])
        queue.remove(square)
        seen[square] = True
        neighbors = adjacencyList[square]
        for neighbor in neighbors:
            potentialDistance = 1 + distances[square]
            distances[neighbor] = min(distances[neighbor], potentialDistance)
            if not seen[neighbor]:
                queue.add(neighbor)
    if distances[100] == float("inf"):
        return -1
    return distances[100]                         

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        mapping = {}
        for ladders_i in range(n):
            start, end = map(int, input().strip().split(' '))
            mapping[start] = end
        m = int(input().strip())
        for snakes_i in range(m):
            start,end = map(int, input().strip().split(' '))
            mapping[start] = end
        result = quickestWayUp(mapping)
        print(result)
