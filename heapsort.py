comparisons = 0
swaps = 0

def heapify(arr, n, i):
    global comparisons, swaps

    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n:
        comparisons += 1
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        comparisons += 1
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        swaps += 1
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    global comparisons, swaps
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        swaps += 1
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr, comparisons, swaps
