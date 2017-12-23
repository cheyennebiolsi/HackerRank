#!/bin/python3

import sys

class Solution:
    def __init__(self, sum, coins):
        self.memo = [[-1 for i in range(len(c))] for j in range(sum + 1)]
        self.sum = sum
        self.coins = coins
        
    def solve(self):
        return self.getWays(self.sum, len(self.coins) - 1)
        
    def getWays(self, sum, coinIndex):
        if coinIndex < 0 or sum < 0:
            return 0
        
        if sum == 0:
            return 1
        
        if self.memo[sum][coinIndex] == -1:
            coin = self.coins[coinIndex]
            numberOfWaysToMakeSumUsingCoin = self.getWays(sum - coin, coinIndex)
            numberOfWaysToMakeSumWithoutUsingCoin = self.getWays(sum, coinIndex - 1)
            self.memo[sum][coinIndex] = numberOfWaysToMakeSumUsingCoin + numberOfWaysToMakeSumWithoutUsingCoin
        return self.memo[sum][coinIndex]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
solution = Solution(n, c)
print(solution.solve())