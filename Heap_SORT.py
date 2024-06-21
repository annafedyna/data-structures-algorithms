def right(i):
    return 2*i + 1


def left(i):
    return 2*i


def parent(i):
    return i // 2


def build_max_heap(a):
    heap_size = len(a)

    for i in range(heap_size//2, 0, -1):
        max_heapify(a, heap_size, i)


def max_heapify(a, heap_size, i):
    l = left(i)
    r = right(i)

    largest = i

    if r < heap_size and a[r] > a[i]:
        largest = r

    if l < heap_size and a[l] > a[largest]:
        largest = l

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)


def heap_sort(a):
    build_max_heap(a)

    for i in range(len(a)-1, 1, -1):
        a[1], a[i] = a[i], a[1]
        max_heapify(a, i, 1)


a = [None, 1, 3, 2, 4, 6, 5]
heap_sort(a)
print(a)
