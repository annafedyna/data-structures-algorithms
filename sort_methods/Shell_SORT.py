def shell_sort(arr):
    gap = (len(arr)+1)//2
    while gap > 0:
        for i in range(gap, len(arr)):
            if arr[i] < arr[i-gap]:
                temp = arr[i]
                arr[i] = arr[i-gap]
                arr[i-gap] = temp
        gap -= 1
    return arr


print(shell_sort([3, 4, 6, 2, 1, 5, 0]))
