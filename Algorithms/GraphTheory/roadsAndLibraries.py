#!/bin/python3

import sys
import copy

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        self.visited = False
        
    def addNeighbor(self, other):
        self.neighbors.append(other)
        other.neighbors.append(self)

class Solution:
    def solve(self, c_lib, c_road, nodes):
        if c_lib < c_road:
            return c_lib*len(nodes)
        
        totalCost = 0
        for node in nodes:
            if not node.visited:
                citiesInConnectedSegment = self.dfs(node)
                totalCost += c_road*(citiesInConnectedSegment - 1) + c_lib
        return totalCost
        
    def dfs(self, node):
        stack = [node]
        numberConnectedNodes = 0
        while (len(stack) > 0):
            node = stack.pop()
            if node.visited:
                continue
            node.visited = True
            numberConnectedNodes += 1
            for neighbor in node.neighbors:
                if not neighbor.visited:
                    stack.append(neighbor)
        return numberConnectedNodes
    

q = int(input().strip())
solution = Solution()
for a0 in range(q):
    n, m, x, y = input().strip().split(' ')
    n, m, x, y = [int(n), int(m), int(x), int(y)]
    nodes = [Node(id) for id in range(1, n+1)]
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        nodes[city_1 - 1].addNeighbor(nodes[city_2 - 1])
    print(solution.solve(x, y, nodes))
