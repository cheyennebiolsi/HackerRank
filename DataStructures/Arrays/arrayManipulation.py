#!/bin/python3

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    differences = [0 for i in range(n)]
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        differences[a-1] += k
        if b <= n - 1:
            differences[b] -= k
    sum = 0
    max = 0
    for difference in differences:
        sum += difference
        if sum > max:
            max = sum
    print(max)
        
