import time
import numpy as np
import matplotlib.pyplot as plt

def bubblesort(array):
    n = len(array) -1
    while n > 0:
        for i in range(n):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
            i = i+1
        n = n-1
        
sorts = [
    {
        "Name" : "bubble sort",
        "Sort" : lambda arr: bubblesort(arr)
    }
]
elements = np.array([i*1000 for i in range(1,5)])
plt.xlabel('List Length')
plt.ylabel('Time Complexity')

for sort in sorts:
    time_taken = []
for sort in sorts:
    start_all = time.time()
    for i in range(1, 5):
        start = time.time()
        a = np.random.randint(0, 1000, i*1000)
        sort["Sort"](a)
        end = time.time()
        time_taken.append(end-start)
        print(sort["Name"], "sorted all elements in", end-start, "s")
    end_all = time.time()
    print(sort["Name"], "sorted all elements in", end_all-start_all, "s")
    plt.plot(elements, time_taken, label=sort["Name"])
        
plt.grid()
plt.legend()
plt.show()
