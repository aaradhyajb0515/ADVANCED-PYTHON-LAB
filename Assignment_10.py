import numpy as np

arr = np.arange(1, 11)

print("Original array:", arr)

print("First 5 elements:", arr[:5])
print("Elements from index 5 to 9:", arr[5:10])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

arr = arr + 2

print("Modified array:", arr)
