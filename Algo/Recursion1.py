def factorialRecursive(n):
    if n == 1:
        return 1
    return n*factorialRecursive(n-1)

def factorialIterative(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial*i
    return factorial

print(factorialRecursive(4))
print(factorialIterative(5))
