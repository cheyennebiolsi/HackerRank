#Note: not actually using trie"

from collections import Counter

class Solution:
    def __init__(self):
        self.directory = Counter()

    def add(self, contact):
        for endIndex in range(1, len(contact) + 1):
            partial = contact[:endIndex]
            self.directory[partial] += 1
            
    def find(self, contact):
        return self.directory[contact]

n = int(input().strip())
solution = Solution()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
        solution.add(contact)
    else:
        print(solution.find(contact))
    
