def quicksort(data):
  if len(data) < 2:
    return data

  pivot = data[0]
  left = [i for i in data[1:] if i <= pivot]
  right = [i for i in data[1:] if i > pivot]

  return quicksort(left) + [pivot] + quicksort(right)

data = [8, 3, 1, 4, 2, 7, 6, 5]
sorted_data = quicksort(data)
print(sorted_data)  
