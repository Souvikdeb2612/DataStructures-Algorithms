#Fibonacci function without dynamic programming

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

#Fibonacci function with dynamic programming

def fibonacci1():
    cache = {}
    def fibo(n):

        if n in cache:
            return cache[n]
        elif n < 2:
            print('time')
            cache[n] = n
            return cache[n]
        else:
            print('time')
            cache[n] = fibo(n - 1) + fibo(n - 2)
            return cache[n]
    return fibo

fib = fibonacci1()
print(fib(7))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(7))
print(fib(9))


#Fibonacci function with bottom up approach

def fibonacci2(n):
   answer = [0, 1]
   for i in range(2, n+1):
       answer.append(answer[i-1]+answer[i-2])

   return answer[n]

print(fibonacci2(3))
print(fibonacci2(9))