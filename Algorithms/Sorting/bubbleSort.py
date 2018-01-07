def swap(arr, i, j):
    firstVal = arr[i]
    secondVal = arr[j]
    if secondVal < firstVal:
        arr[i] = secondVal
        arr[j] = firstVal
        return 1
    return 0

def bubbleSort(arr):
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            swaps += swap(arr, j, j+1)
    return swaps

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swaps = bubbleSort(a)
print("Array is sorted in {} swaps.".format(swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
