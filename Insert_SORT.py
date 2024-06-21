def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
    return arr


print(insert_sort([1, 4, 3, 2, 5]))
