def fibonacci(n, values):
    if n == 0 or n == 1:
        return n
    if n not in values:
        values[n] = fibonacci(n - 1, values) + fibonacci(n - 2, values)
    return values[n]
    
# Write your code here.
n = int(input())
print(fibonacci(n, {}))
