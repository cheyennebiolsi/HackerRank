#!/bin/python3

import sys

def lonely_integer(a):
    value = 0
    for val in a:
        value ^= val
    return value

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
