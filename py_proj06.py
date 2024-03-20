import time
import numpy as np
import matplotlib.pyplot as plt

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            print("Search is success at position", i)
            return True
    print("Search is not success")
    return False

elements = np.array([i*1000 for i in range(1, 40)])
plt.xlabel("List Length")
plt.ylabel("Time Complexity (s)")

times = []
for i in range(1, 40):
    start = time.time()
    a = np.sort(np.random.randint(1000, size=i*1000))  # Sort the list for better time complexity
    linear_search(a, 1)
    end = time.time()
    times.append(end-start)
    print(f"Time taken for linear search of {i*1000} elements is {end-start} s")

plt.plot(elements, times, label="Linear Search")
plt.grid()
plt.legend()
plt.show()