#Insertion Sort

def insertionSort(N):
    for i in range(1, len(N)):
        last_sort = N[i]
        while N[i-1] > last_sort and i > 0:
            print(N[i])
            print(N)
            N[i], N[i-1] = N[i-1], N[i]
            i = i -1
    return N

N = [55, 2, 3, 6, 1, 9, 4, 7, 10,5, 5, 8, 11]
print(insertionSort(N))






