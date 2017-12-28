#!/bin/python3

import sys

def getDistances(nodes, startingNode):
    queue = [node for node in nodes]
    distances = [float("inf") if node != startingNode else 0 for node in nodes]
    
    while len(queue) > 0:
        node = min(queue, key=lambda x: distances[x.id - 1])
        queue.remove(node)
        for neighbor, distance in node.neighbors:
            alternativePath = distances[node.id - 1] + distance
            if alternativePath < distances[neighbor.id - 1]:
                distances[neighbor.id - 1] = alternativePath
                
    distances = [str(distance) if distance != float("inf") else "-1" for distance in distances]
    del distances[startingNode.id - 1]
    return " ".join(distances)

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        
    def addNeighbor(self, other, distance):
        self.neighbors.append((other, distance))
        other.neighbors.append((self, distance))
        
    def __hash__(self):
        return self.id

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        nodes = [Node(id) for id in range(1, n+1)]
        for a1 in range(m):
            u, v = input().strip().split(' ')
            u, v = [int(u), int(v)]
            nodes[u-1].addNeighbor(nodes[v-1], 6)
        s = int(input().strip())
        startingNode = nodes[s-1]
        print(getDistances(nodes, startingNode))