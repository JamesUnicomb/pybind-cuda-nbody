import gpu_library
import numpy as np
import time

size = 10000000
arr1 = np.linspace(1.0,100.0, size)
arr2 = np.linspace(1.0,100.0, size)

runs = 10
factor = 1.1

t0 = time.time()
for _ in range(runs):
    gpu_library.multiply_with_scalar(arr1, factor)
print("gpu time: " + str(time.time()-t0))
t0 = time.time()
for _ in range(runs):
    for i in range(1000):
        arr2 = arr2 * factor
print("cpu time: " + str(time.time()-t0))

print("results match: " + str(np.allclose(arr1,arr2)))