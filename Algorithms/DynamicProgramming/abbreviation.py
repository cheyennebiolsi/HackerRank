#!/bin/python3

import sys

def abbreviation(a, b):
    memoized = [[0 for i in range(len(b))] for j in range(len(a))]
    for aIndex in range(len(a)):
        aChar = a[aIndex]
        if aChar != b[0] and aChar.upper() != b[0]:
            if aChar.isupper():
                return "NO"
        else:
            startIndex = aIndex
            break

    for aIndex in range(startIndex, len(a)):
        aChar = a[aIndex]
        for bIndex in range(len(b)):
            bChar = b[bIndex]
            if aChar.islower():
                memoized[aIndex][bIndex] = memoized[aIndex - 1][bIndex]
            if (aChar == bChar or aChar.upper() == bChar):
                if bIndex > 0:
                    memoized[aIndex][bIndex] = max(memoized[aIndex][bIndex], int(memoized[aIndex - 1][bIndex - 1] == 1))
                else:
                    memoized[aIndex][bIndex] = 1

    if memoized[aIndex][len(b) - 1]:
            return "YES"
    return "NO"
    

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a = input().strip()
        b = input().strip()
        result = abbreviation(a, b)
        print(result)
