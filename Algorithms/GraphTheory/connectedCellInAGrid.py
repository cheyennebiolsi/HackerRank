class Solution:
    def __init__(self, grid):
        self.grid = grid
        self.seen = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
        
    def getBiggestRegion(self):
        sizes = set()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.seen[i][j] == 1 or self.grid[i][j] == 0:
                    continue
                sizes.add(self.dfs(i, j))
        return max(sizes)
                
    def dfs(self, i, j):
        if i < 0 or j < 0:
            return 0
        if i >= len(self.seen) or j >= len(self.seen[0]):
            return 0
        if self.seen[i][j] == 1:
            return 0
        self.seen[i][j] = 1
        if self.grid[i][j] == 0:
            return 0
        value = 1
        for nextI in (i, i+1, i-1):
            for nextJ in (j, j+1, j-1):
                value += self.dfs(nextI, nextJ)
        return value
    

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
solution = Solution(grid)
print(solution.getBiggestRegion())