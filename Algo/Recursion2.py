def fibonacciRecursive(n):
    if n < 2:
        return n
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

print(fibonacciRecursive(6))

def fibonacciIterative(n):
    a = 0
    b = 1
    sum = 0
    if n < 2:
        return n
    for i in range(2, n+1):
        sum = a + b
        a = b
        b = sum
    return sum

print(fibonacciIterative(6))
