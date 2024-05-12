import time
import numpy as np
import matplotlib.pyplot as plt
def binary_search(arr, target):
    arr = sorted(arr)
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) //2
        if target < arr[mid]:
            high = mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1
elements = np.array([i*1000 for i in range(1,40)])
plt.xlabel('List Length')
plt.ylabel('Time Complexity')
times = []
for i in range(1, 40):
    start = time.time()
    a = np.random.randint(1000, size = i*1000)
    binary_search(a, 1)
    end = time.time()
    times.append(end-start)
    print("Time taken for Binary Search on", i*1000, "elements is", end-start, "s")
plt.plot(elements, times, label="Binary Search")
plt.grid()
plt.legend()
plt.show()
