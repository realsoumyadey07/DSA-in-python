def insertionSort(arr):
    for i in range(1, len(arr)):
        a = arr[i]
        j = i-1
        while j >=0 and arr[j]>a:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = a
    return arr

arr = [8,2,4,9,1,5,3]
print(insertionSort(arr))