import random  # For randomized pivot selection and random array generation
import timeit  # For benchmarking running time
import numpy as np  # For computing average times
import matplotlib.pyplot as plt  # For plotting results
import sys  # For setting recursion limit

# Increase recursion limit to handle inputs up to size 1000
sys.setrecursionlimit(2000)

def median_of_three(arr, low, high):
    """
    Selects the median of the first, middle, and last elements as the pivot.
    Swaps the median with the last element for partitioning.
    
    Args:
        arr (list): The array
        low (int): Starting index of the subarray
        high (int): Ending index of the subarray
    """
    mid = (low + high) // 2
    candidates = [
        (arr[low], low),
        (arr[mid], mid),
        (arr[high], high)
    ]
    candidates.sort()  # Sort by value to find median
    median_index = candidates[1][1]  # Middle value’s index
    arr[median_index], arr[high] = arr[high], arr[median_index]

def three_way_partition(arr, low, high, randomized=False):
    """
    Partitions the array into three parts: < pivot, == pivot, > pivot.
    Returns the boundaries of the equal-to-pivot section.
    
    Args:
        arr (list): The array to be partitioned
        low (int): Starting index of the subarray
        high (int): Ending index of the subarray
        randomized (bool): If True, selects a random pivot
    
    Returns:
        tuple: (left, right) indices where equal-to-pivot elements lie
    """
    if randomized:
        rand_index = random.randint(low, high)
        arr[rand_index], arr[high] = arr[high], arr[rand_index]
    else:
        median_of_three(arr, low, high)  # Use median-of-three for deterministic
    
    pivot = arr[high]
    i = low  # Iterator for scanning
    lt = low  # Boundary for < pivot
    gt = high  # Boundary for > pivot
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    
    return lt, gt

def quicksort(arr, low, high, randomized=False):
    """
    Recursively sorts the array using Quicksort with three-way partitioning.
    Supports deterministic (median-of-three) and randomized pivot selection.
    
    Args:
        arr (list): The array to be sorted
        low (int): Starting index of the subarray
        high (int): Ending index of the subarray
        randomized (bool): If True, selects a random pivot
    """
    if low < high:
        lt, gt = three_way_partition(arr, low, high, randomized)
        quicksort(arr, low, lt - 1, randomized)
        quicksort(arr, gt + 1, high, randomized)

def sort(arr, randomized=False):
    """
    Wrapper function to sort the entire array using Quicksort.
    Handles edge cases like empty or single-element arrays.
    
    Args:
        arr (list): The array to be sorted
        randomized (bool): If True, uses randomized pivot selection
    
    Returns:
        list: The sorted array
    """
    if arr:
        quicksort(arr, 0, len(arr) - 1, randomized)
    return arr

def generate_data(size, order='random'):
    """
    Generates an array of size n based on the specified type.
    
    Args:
        size (int): Size of the array
        order (str): Type of array ('random', 'sorted', 'reverse', 'equal')
    
    Returns:
        list: The generated array
    
    Raises:
        ValueError: If an invalid array type is provided
    """
    if order == 'sorted':
        return list(range(size))
    elif order == 'reverse':
        return list(range(size, 0, -1))
    elif order == 'equal':
        return [1] * size
    else:
        return np.random.randint(0, size * 10, size).tolist()

def plot_results(results):
    """
    Generates plots comparing deterministic and randomized Quicksort running times.
    Creates a separate plot for each input distribution.
    
    Args:
        results (dict): Experimental results with running times
    """
    sizes = [100, 500, 1000]  # Match benchmark sizes
    dists = ['random', 'sorted', 'reverse', 'equal']
    for dist in dists:
        det_times = [results[size][dist][0] for size in sizes]
        rand_times = [results[size][dist][1] for size in sizes]
        plt.figure()
        plt.plot(sizes, det_times, label='Deterministic (Median-of-Three)', marker='o')
        plt.plot(sizes, rand_times, label='Randomized', marker='s')
        plt.xlabel('Array Size')
        plt.ylabel('Time (seconds)')
        plt.title(f'Quicksort Running Time for {dist.capitalize()} Arrays')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'{dist}_plot.png')
        plt.close()

def run_benchmarks():
    """
    Runs benchmarks to compare deterministic and randomized Quicksort.
    Tests different array sizes and input distributions, and generates plots.
    
    Returns:
        dict: Results mapping sizes to input types and their running times
    """
    sizes = [100, 500, 1000]  # Match your tested sizes
    dists = ['random', 'sorted', 'reverse', 'equal']
    results = {size: {} for size in sizes}
    
    for size in sizes:
        print(f"\n--- Array Size: {size} ---")
        for dist in dists:
            if dist == 'random':
                d_times = []
                r_times = []
                for _ in range(10):
                    data = generate_data(size, order=dist)
                    d_times.append(timeit.timeit(lambda: sort(data.copy(), randomized=False), number=1))
                    r_times.append(timeit.timeit(lambda: sort(data.copy(), randomized=True), number=1))
                d_time = np.mean(d_times)
                r_time = np.mean(r_times)
            else:
                data = generate_data(size, order=dist)
                d_time = timeit.timeit(lambda: sort(data.copy(), randomized=False), number=10) / 10
                r_time = timeit.timeit(lambda: sort(data.copy(), randomized=True), number=10) / 10
            results[size][dist] = (d_time, r_time)
            print(f"{dist.capitalize():<10} | Deterministic: {d_time:.4f}s | Randomized: {r_time:.4f}s")
    
    plot_results(results)
    print("\nPlots generated: random_plot.png, sorted_plot.png, reverse_plot.png, equal_plot.png")
    return results

if __name__ == "__main__":
    # Run benchmarks
    run_benchmarks()
    
    # Test edge cases
    print("\nEdge Case Tests:")
    empty = []
    sort(empty, randomized=False)
    print("Empty array:", empty)
    
    single = [42]
    sort(single, randomized=True)
    print("Single element:", single)
    
    duplicates = [5, 5, 5, 5]
    sort(duplicates, randomized=False)
    print("All duplicates:", duplicates)