import random
import time
from src.heapsort import heap_sort

sizes = [1,2,3,4,5,10,250,999,9999,89786,789300,1780000]

for size in sizes:

    data = [random.randint(1,1000000) for _ in range(size)]

    start = time.time()

    sorted_list, comparisons, swaps = heap_sort(data)

    end = time.time()

    print("Size:", size)
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)
    print("Execution Time:", end-start)
    print("--------------------------------")