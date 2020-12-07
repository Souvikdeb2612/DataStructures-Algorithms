
#Finding the first recurring element in an array

A = [1, 3, 3, 1 , 1, 7, 8]
print("The array given is: {}".format(A))
def bruteForce(A):
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if (A[i]==A[j]):
                return A[i]
                break

    return "undefined"

print("Using bruteForce: {}".format(bruteForce(A)))

h = {}

def hashTable(A):
    for i in A:
       if i in h:
            return i
            break

       else:
            h[i]=0
    return "undefined"

print("Using HashTable: {}".format(hashTable(A)))