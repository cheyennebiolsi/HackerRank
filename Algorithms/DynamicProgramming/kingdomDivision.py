# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from enum import Enum

class Color(Enum):
    NONE = 2
    RED = 0
    BLUE = 1

class Solution:
    def __init__(self, cities):
        self.cities = cities
        self.memo = [[[-1 for i in range(3)] for j in range(3)] for city in range(len(cities))]
        
    def solve(self):
        combinationsIfRootIsRed = self.count(1, Color.RED, Color.NONE) % (10**9 + 7)
        combinationsIfRootIsBlue = self.count(1, Color.BLUE, Color.NONE) % (10**9 + 7)
        return ((combinationsIfRootIsRed + combinationsIfRootIsBlue) % (10**9 + 7))
        
    def count(self, cityId, cityColor, parentColor): 
        city = self.cities[cityId - 1]       
        city.visited = True
        if self.memo[cityId - 1][cityColor.value][parentColor.value] == -1:  
            #Combinations if city is cityColor
            combinations = 1
            combinationsWhereAllChildrenAreBlue = 1
            combinationsWhereAllChildrenAreRed = 1
            for child in city.neighbors:
                if child.visited:
                    continue
                combinationsIfChildIsBlue =  self.count(child.id, Color.BLUE, cityColor)
                combinationsIfChildIsRed = self.count(child.id, Color.RED, cityColor)
                combinations *= (combinationsIfChildIsBlue + combinationsIfChildIsRed)
                combinationsWhereAllChildrenAreBlue *= combinationsIfChildIsBlue
                combinationsWhereAllChildrenAreRed *= combinationsIfChildIsRed

            if cityColor != parentColor:
                if cityColor == Color.RED:
                    combinations -= combinationsWhereAllChildrenAreBlue
                else:
                    combinations -= combinationsWhereAllChildrenAreRed
            self.memo[cityId - 1][cityColor.value][parentColor.value] = combinations
          
        city.visited = False
        return self.memo[cityId - 1][cityColor.value][parentColor.value]


class City:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        self.visited = False
        
    def addNeighbor(self, other):
        self.neighbors.append(other)
        other.neighbors.append(self)

numCities = int(input().strip())
cities = [City(id) for id in range(1, numCities + 1)]
for i in range(numCities - 1):
    parentId, childId = map(int, input().strip().split(' '))
    cities[parentId - 1].addNeighbor(cities[childId - 1])
solution = Solution(cities)
print(solution.solve())