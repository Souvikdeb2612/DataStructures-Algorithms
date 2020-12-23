
#Function without Memoization
def add80(n):
  print('Long time')
  return n+80

print(add80(5))
print(add80(5))

#Function with Memoization
def memoizationadd80():
    cache = {}
    def memoized(n):

        if n in cache:
            return cache[n]
        else:
            print('Long time')
            cache[n] = n + 80
            return cache[n]
    return memoized

memo = memoizationadd80()

print(memo(5))
print(memo(6))
print(memo(5))
print(memo(8))
print(memo(6))
print(memo(9))
print(memo(5))
print(memo(5))
print(memo(6))