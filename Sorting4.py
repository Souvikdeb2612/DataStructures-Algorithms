#Merge Sort
def merge(left, right):
    result = []
    i, j =0, 0
    while i < len(left) and j < len(right):
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
        else:
            result.append(left[i])
            i+=1

    result += left[i:]
    result += right[j:]
    #print("result:{}".format(result))

    return result
def mergeSort(N):

    if len(N)==1:
        return N
    else:
        mid = int(len(N)/2)
        left = mergeSort(N[:mid])
        #print("left:{}" .format(left))
        right = mergeSort(N[mid:])
        #print("right:{}" .format(right))
        return merge(left,right)




N = [55, 2, 3, 6, 9, 32, 43, 6, 9, 37, 372, 8, 1, 0]
print(mergeSort(N))

