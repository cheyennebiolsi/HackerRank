# Enter your code here. Read input from STDIN. Print output to STDOUT

class Solution:
    def __init__(self, t_1, t_2, n):
        self.n = n
        self.memoized = [-1 for i in range(n+1)]
        self.memoized[1] = t_1
        self.memoized[2] = t_2
        
    def solve(self):
        return self.fibonacci(self.n)
    
    def fibonacci(self, n):
        if self.memoized[n] == -1:
            self.memoized[n] = self.fibonacci(n-2) + (self.fibonacci(n-1)**2)
        return self.memoized[n]        

t_1, t_2, n = map(int, input().strip().split(' '))
print(Solution(t_1, t_2, n).solve())