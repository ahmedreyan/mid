import time
import numpy as np
import matplotlib.pyplot as plt

def selectionsort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

sorts = [
    {
        "Name" : "Selection Sort",
        "sort" : lambda arr: selectionsort(arr)
    }
]
elements = np.array([i*1000 for i in range(1,5)])
plt.xlabel('List Length')
plt.ylabel('Time Complexity')

times = []
for sort in sorts:
    start_all = time.time()
    for i in range(1, 5):
        start = time.time()
        a = np.random.randint(0, 1000, i*1000)
        sort["sort"](a)
        end = time.time()
        times.append(end-start)
        print(sort["Name"], "sorted all elements in", end-start, "s")
    end_all = time.time()
    print(sort["Name"], "sorted all elements in", end_all-start_all, "s")
    plt.plot(elements, times, label=sort["Name"])

plt.grid()
plt.legend()
plt.show()
