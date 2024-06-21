def selection_sort(arr):
    for i in range(len(arr)):
        pointer1 = i
        for j in range(i, len(arr)):
            if arr[j] < arr[pointer1]:
                pointer1 = j
        arr[i], arr[pointer1] = arr[pointer1], arr[i]
    return arr


print(selection_sort([3, 4, 2, 1, 5, 6]))
