from heapq import heapify, heappop, heappush

def getTotalWeight(edges, nodes):
    startingEdge = min(edges)
    totalCost = 0
    uncheckedEdges = [startingEdge]
    heapify(uncheckedEdges)
    
    while len(uncheckedEdges) > 0:
        minEdge = heappop(uncheckedEdges)
        if minEdge.visited:
            continue
        minEdge.visited = True
        if minEdge.hasUnvisitedEndpoint():
            totalCost += minEdge.cost
        for node in minEdge.endpoints:
            if not node.visited:
                node.visited = True
                for edge in node.edges:
                    if not edge.visited:
                        heappush(uncheckedEdges, edge)
                        
    return totalCost    

class Edge:
    def __init__(self, u, v, cost):
        self.endpoints = [u, v]
        self.cost = cost
        self.specialWeight = u.id + v.id + cost
        self.visited = False
    
    def __lt__(self, other):
        if self.cost == other.cost:
            return self.specialWeight < other.specialWeight
        return self.cost < other.cost
    
    def hasUnvisitedEndpoint(self):
        for node in self.endpoints:
            if not node.visited:
                return True
        return False            

class Node:
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.visited = False
        
    def addEdge(self, other, edge):
        self.edges.append(edge)
        other.edges.append(edge)

n, m = map(int, input().strip().split(' '))
nodes = [Node(id) for id in range(1, n+1)]
edges = []
for i in range(m):
    endA, endB, cost = map(int, input().strip().split(' '))
    u = nodes[endA - 1]
    v = nodes[endB - 1]
    edge = Edge(u, v, cost)
    edges.append(edge)
    u.addEdge(v, edge)
print(getTotalWeight(edges, nodes))
    
    