# Selection sort

def selectionSort(N):
    for i in range(len(N)-1):
        min = N[i]
        min_index = i
        for j in range(i+1,len(N)):
            if N[j]<min:
                min = N[j]
                min_index = j
        if min_index != i:
            N[min_index], N[i] = N[i], N[min_index]
    return N


N = [55, 2, 3, 6, 1, 9, 4, 7, 10, 5, 8, 11]
print(selectionSort(N))