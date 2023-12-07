import random
import time
import matplotlib.pyplot as plt
from merge_sort import MergeSort
from quick_sort import QuickSort

# Generate test arrays
lengths = [10000, 30000, 50000, 80000, 100000, 200000]
test_arrays = [random.sample(range(1, length * 10), length) for length in lengths]

# Time the algorithms
merge_sort_times = []
quick_sort_times = []

merge_sorter = MergeSort()
quick_sorter = QuickSort()

for test_array in test_arrays:
    # Time Merge Sort
    array_copy = test_array.copy()
    start_time = time.time()
    merge_sorter.sort(array_copy)
    merge_sort_times.append(time.time() - start_time)

    # Time QuickSort
    array_copy = test_array.copy()
    start_time = time.time()
    quick_sorter.sort(array_copy)
    quick_sort_times.append(time.time() - start_time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(lengths, merge_sort_times, '-o', label='Merge Sort')
plt.plot(lengths, quick_sort_times, '-o', label='Quick Sort')
plt.xlabel('Array Length')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Merge Sort vs. Quick Sort')
plt.legend()
plt.grid(True)
plt.show()
