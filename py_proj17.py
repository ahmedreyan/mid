from heapq import merge
import time
import numpy as np
import matplotlib.pyplot as plt

def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        l = array[:mid]
        r = array[mid:]

        mergesort(l)
        mergesort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1   

        while j < len(r): 
            array[k] = r[j]
            j += 1
            k += 1 

elements = np.array([i*1000 for i in range(1,10)])
plt.xlabel('List Length')
plt.ylabel('Time Complexity')
times = []
for i in range(1, 10):
    start = time.time()
    a = np.random.randint(1000, size=i*1000)
    mergesort(a)
    end = time.time()
    times.append(end-start)
    print("Merge Sort sorted all elements in", end-start, "s")        
plt.plot(elements, times, label="Merge Sort")
plt.grid()
plt.legend()
plt.show()
