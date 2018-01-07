class Solution:
    def __init__(self):
        self.memoized = {1: 1, 2: 2, 3: 4}
        
    def getWays(self, steps):
        if steps in self.memoized:
            return self.memoized[steps]
        number = self.getWays(steps - 1) + self.getWays(steps - 2) + self.getWays(steps - 3)
        self.memoized[steps] = number
        return number

s = int(input().strip())
solution = Solution()
for a0 in range(s):
    n = int(input().strip())
    print(solution.getWays(n))