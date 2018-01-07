#!/bin/python3

import sys

def countInversions(arr):
    # Complete this function
    return mergeSort(arr, 0, len(arr) - 1)[1]
    
def mergeSort(arr, startPoint, endPoint):
    if endPoint - startPoint < 0:
        return [], 0
    if endPoint - startPoint == 0:
        return arr[startPoint: endPoint + 1], 0
    if endPoint - startPoint == 1:
        return mergeAndCount(arr[startPoint:startPoint + 1], arr[endPoint:endPoint + 1])
    
    midPoint = (endPoint + startPoint)//2
    lowerHalf, lowerInversions = mergeSort(arr, startPoint, midPoint)
    upperHalf, upperInversions = mergeSort(arr, midPoint + 1, endPoint)
    merged, inversions = mergeAndCount(lowerHalf, upperHalf)
    return merged, lowerInversions + upperInversions + inversions
    
def mergeAndCount(lowerHalf, upperHalf):
    arr = []
    index1 = 0
    index2 = 0
    inversions = 0
    while index1 < len(lowerHalf) and index2 < len(upperHalf):
        lowerVal = lowerHalf[index1]
        upperVal = upperHalf[index2]            
        if upperVal < lowerVal:
            arr.append(upperVal)
            index2 += 1
            inversions += (len(lowerHalf) - (index1))
        else:
            arr.append(lowerVal)
            index1 += 1
    if index1 == len(lowerHalf):
        arr += upperHalf[index2:]
    if index2 == len(upperHalf):
        arr += lowerHalf[index1:]
    return arr, inversions

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)
