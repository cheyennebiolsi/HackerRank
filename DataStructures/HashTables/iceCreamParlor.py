#!/bin/python3

import sys

def solve(arr, money):
    priceToId = {}
    for index, price in enumerate(arr):
        otherPrice = money - price
        if otherPrice in priceToId:
            values = list(map(str, sorted([index + 1, priceToId[otherPrice]])))
            return " ".join(values)
        priceToId[price] = index + 1

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        print(solve(arr, money))

