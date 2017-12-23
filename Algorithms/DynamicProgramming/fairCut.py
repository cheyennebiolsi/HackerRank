# Enter your code here. Read input from STDIN. Print output to STDOUT


class Solution:
    def __init__(self, arr, k,n):
        self.arr = arr
        self.k = k
        self.n = n
        
    def solve(self):
        #memoized[a][j] represents having given out up to (but not including) a presents, j of which
        #went to Li
        memoized = [[float("inf") for i in range(self.n + 1)] for j in range(self.n + 1)]
        memoized[0][0] = 0
        
        for index, value in enumerate(self.arr):
            for numbersOwnedByLi in range(0, index + 1):
                numbersOwnedByLu = index - numbersOwnedByLi
                numbersLeftToBeAssignedToLi = self.k - numbersOwnedByLi
                numbersLeftToBeAssignedToLu = self.n - self.k - numbersOwnedByLu
                if numbersOwnedByLi > self.k or numbersOwnedByLu > self.n - self.k:
                    continue
                
                #Give to Li:
                contributionForGivingToLi = memoized[index][numbersOwnedByLi] + value*(numbersOwnedByLu) - value*(numbersLeftToBeAssignedToLu)
                if memoized[index + 1][numbersOwnedByLi + 1] > contributionForGivingToLi:
                    memoized[index + 1][numbersOwnedByLi + 1] = contributionForGivingToLi
                
                #Give to Lu
                contributionForGivingToLu = memoized[index][numbersOwnedByLi] + value*numbersOwnedByLi - value*numbersLeftToBeAssignedToLi
                if memoized[index + 1][numbersOwnedByLi] > contributionForGivingToLu:
                    memoized[index + 1][numbersOwnedByLi] = contributionForGivingToLu
                    
        return memoized[self.n][self.k]    
                        

numElements, k = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split(' ')))
print(Solution(sorted(arr), k, numElements).solve())