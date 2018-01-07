import math

def printPrimality(n):
    if n == 1:
        print("Not prime")
        return
    if n == 2 or n == 3:
        print("Prime")
        return
    squareRoot = int(math.ceil(math.sqrt(n)))
    for i in range(2, squareRoot + 1):
        if n % i == 0:
            print("Not prime")
            return
    print("Prime")

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    printPrimality(n)
