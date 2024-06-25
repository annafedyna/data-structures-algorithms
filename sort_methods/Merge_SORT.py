'''
Time Complexity : O(n*logn)
'''

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    middle = len(arr)//2
    
    left_part = merge_sort(arr[:middle])
    right_part = merge_sort(arr[middle:])

    return merge(left_part, right_part)

def merge(left_part, right_part):
    res = []
    
    while left_part and right_part:
        if left_part[0] < right_part[0]:
            res.append(left_part[0])
            left_part.pop(0)
        else:
            res.append(right_part[0])
            right_part.pop(0)
    
    if left_part:
        for el in left_part:
            res.append(el)
    else:
        for el in right_part:
            res.append(el)

    return res

print(merge_sort([2,3,1,4,0,5]))