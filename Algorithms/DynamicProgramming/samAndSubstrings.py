# Enter your code here. Read input from STDIN. Print output to STDOUT

class Solution:
    def solve(self, string):
        previousValue = int(string[0])
        currentValue = previousValue
        for index in range(1, len(string)):
            additionalValue = previousValue * 10 + int(string[index]) * (index + 1)
            currentValue += additionalValue
            previousValue = additionalValue
        return currentValue % (10**9 + 7)


string = input().strip()
solution = Solution()
print(solution.solve(string))
