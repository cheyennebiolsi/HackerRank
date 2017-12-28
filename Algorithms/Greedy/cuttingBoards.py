def minimizeCosts(verticalCosts, horizontalCosts):
    totalCosts = 0
    horizontalIndex = 0
    verticalIndex = 0
    horizontalCost = horizontalCosts[0]
    verticalCost = verticalCosts[0]
    while horizontalIndex < len(horizontalCosts) or verticalIndex < len(verticalCosts):
        if horizontalCost > verticalCost:
            totalCosts += horizontalCost * (verticalIndex + 1)
            horizontalIndex += 1
            if horizontalIndex < len(horizontalCosts):
                horizontalCost = horizontalCosts[horizontalIndex]
            else:
                horizontalCost = -float("inf")
        else:
            totalCosts += verticalCost * (horizontalIndex + 1)
            verticalIndex += 1
            if verticalIndex < len(verticalCosts):
                verticalCost = verticalCosts[verticalIndex]
            else:
                verticalCost = -float("inf")                
    return totalCosts % (10**9 + 7)
        
queries = int(input().strip())
for q in range(queries):
    vertical, horizontal = map(int, input().strip().split(' '))
    verticalCosts = sorted(list(map(int, input().strip().split(' '))))[::-1]
    horizontalCosts =sorted(list(map(int, input().strip().split(' '))))[::-1]
    print(minimizeCosts(verticalCosts, horizontalCosts))