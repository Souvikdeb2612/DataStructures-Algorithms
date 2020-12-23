# Bubble sort

def bubbleSort(N):
    a = 0
    while a < len(N):
        for i in range(len(N) - 1):
            if N[i] > N[i + 1]:
                N[i + 1], N[i] = N[i], N[i + 1]
        a += 1
    return N

N = [55, 2, 3, 6, 1, 9, 4, 7, 10, 5, 8, 11]
print(bubbleSort(N))

