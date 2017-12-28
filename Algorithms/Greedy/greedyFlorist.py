#!/bin/python3

import sys

def getMinimumCost(n, k, c):
    # Complete this function
    
    person = 0
    timesVisited = 0
    cost = 0
    for basePrice in c[::-1]:
        cost += (timesVisited + 1) * basePrice
        person = (person + 1)%k
        if person == 0:
            timesVisited += 1
    
    return cost
    
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = list(map(int, input().strip().split(' ')))
minimumCost = getMinimumCost(n, k, sorted(c))
print(minimumCost)

