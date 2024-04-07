def selectionSort(arr, size):
    for s in range(size):
        min_idx = s
        for i in range(s+1,size):
            if arr[i] < arr[min_idx]:
                min_idx = i
        (arr[s], arr[min_idx]) = (arr[min_idx], arr[s])

arr = [3,6,1,9,2,5,9]
size = len(arr)

selectionSort(arr, size)

print("The sorted array is: ")
for i in arr:
    print(i)