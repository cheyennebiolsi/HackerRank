def minimizeUnfairness(K, arr):
    minUnfairness = float("inf")
    for k in range(len(arr) - K + 1):
        minUnfairness = min(arr[k + K - 1] - arr[k], minUnfairness)
    return minUnfairness

N = int(input().strip())
K = int(input().strip())
arr = sorted([int(input().strip()) for i in range(N)])
print(minimizeUnfairness(K, arr))