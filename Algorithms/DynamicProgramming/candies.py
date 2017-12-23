#!/bin/python3

import sys

def candies(n, arr):
    candies = [1 for child in range(n)]
    
    for child in range(1, n):
        previousChildRating = arr[child-1]
        childRating = arr[child]
        if childRating > previousChildRating:
            candies[child] = candies[child-1] + 1
        
    for child in range(n-1, 0, -1):
        previousChildRating = arr[child-1]
        childRating = arr[child]
        if previousChildRating > childRating:
            candies[child-1] = max(candies[child] + 1, candies[child-1])
            
    return sum(candies)
        

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
        arr_t = int(input().strip())
        arr.append(arr_t)
    result = candies(n, arr)
    print(result)