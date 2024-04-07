def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [9,2,5,7,1,3]
bubbleSort(arr)

print("The sorted array is: ")
for i in arr:
    print(i)