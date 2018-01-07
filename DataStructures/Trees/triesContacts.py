from collections import Counter

class Node:
    def __init__(self, value):
        self.value = value
        self.count = 0
        self.children = {}

    def add(self):
        self.count += 1

    def getNodeWithValue(self, value):
        if value not in self.children:
            node = Node(value)
            self.children[value] = node
        return self.children[value]

class Trie:
    def __init__(self):
        self.root = Node("ROOT")

    def add(self, contact):
        currentNode = self.root
        for character in contact:
            node = currentNode.getNodeWithValue(character)
            node.add()
            currentNode = node

    def find(self, contact):
        currentNode = self.root
        for character in contact:
            currentNode = currentNode.getNodeWithValue(character)
        return currentNode.count

class Solution:
    def __init__(self):
        self.trie = Trie()

    def add(self, contact):
        self.trie.add(contact)

    def find(self, contact):
        return self.trie.find(contact)

n = int(input().strip())
solution = Solution()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
        solution.add(contact)
    else:
        print(solution.find(contact))
