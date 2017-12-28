"test" 
#!/bin/python3

import sys
from heapq import heapify, heappush, heappop, heappushpop

class MinHeap:
    def __init__(self):
        self.size = 0
        self.minHeap = []
        heapify(self.minHeap)
        
    def push(self, value):
        self.size += 1
        heappush(self.minHeap, value)
        
    def peek(self):
        return self.minHeap[0]
    
    def heappushpop(self, value):
        return heappushpop(self.minHeap, value)
    
class MaxHeap:
    def __init__(self):
        self.size = 0
        self.maxHeap = []
        heapify(self.maxHeap)
        
    def push(self, value):
        self.size += 1
        heappush(self.maxHeap, -value)
        
    def peek(self):
        return -self.maxHeap[0]
    
    def heappushpop(self, value):
        return -heappushpop(self.maxHeap, -value)
    
class Solution:
    def __init__(self):
        self.smallestHalf = MaxHeap()
        self.largestHalf = MinHeap()
        
    def getMedian(self):
        if self.smallestHalf.size == 0 and self.largestHalf.size == 0:
            raise ValueError("Solution not populated: no median value")
        if self.smallestHalf.size > self.largestHalf.size:
            return self.smallestHalf.peek()
        return (self.smallestHalf.peek() + self.largestHalf.peek())/2
    
    def add(self, value):
        largestValueInBottomHalf = self.smallestHalf.heappushpop(value)
        smallestValueInUpperHalf = self.largestHalf.heappushpop(largestValueInBottomHalf)
        if self.smallestHalf.size == self.largestHalf.size:
            self.smallestHalf.push(smallestValueInUpperHalf)
        else:
            self.largestHalf.push(smallestValueInUpperHalf)
        
        

n = int(input().strip())
solution = Solution()
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    solution.add(a_t)
    print("{0:.1f}".format(solution.getMedian()))
