def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr


print(bubble_sort([2, 4, 3, 1, 5, 6]))
