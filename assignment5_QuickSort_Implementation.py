import random  # For randomized pivot selection

def partition(arr, low, high):
    """
    Partitions the array around the pivot (last element).
    Places elements <= pivot to the left and > pivot to the right.
    
    Args:
        arr (list): The array to be partitioned
        low (int): Starting index of the subarray
        high (int): Ending index of the subarray
    
    Returns:
        int: The final index of the pivot
    """
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1  # Index of the smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in correct position
    return i + 1

def quicksort(arr, low, high, randomized=False):
    """
    Recursively sorts the array using Quicksort.
    Supports both deterministic and randomized pivot selection.
    
    Args:
        arr (list): The array to be sorted
        low (int): Starting index of the subarray
        high (int): Ending index of the subarray
        randomized (bool): If True, selects a random pivot; else, uses last element
    """
    if low < high:
        if randomized:
            # Select a random pivot and swap it with the last element
            rand_index = random.randint(low, high)
            arr[rand_index], arr[high] = arr[high], arr[rand_index]
        
        # Get the pivot's final position
        pi = partition(arr, low, high)
        
        # Recursively sort the left and right subarrays
        quicksort(arr, low, pi - 1, randomized)
        quicksort(arr, pi + 1, high, randomized)

def sort(arr, randomized=False):
    """
    Wrapper function to sort the entire array.
    Handles edge cases like empty or single-element arrays.
    
    Args:
        arr (list): The array to be sorted
        randomized (bool): If True, uses randomized Quicksort
    """
    if arr:  # Check for non-empty array
        quicksort(arr, 0, len(arr) - 1, randomized)

# Example usage and testing
if __name__ == "__main__":
    # Test deterministic Quicksort
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    sort(arr1, randomized=False)
    print("Deterministic Quicksort:", arr1)
    
    # Test randomized Quicksort
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    sort(arr2, randomized=True)
    print("Randomized Quicksort:", arr2)
    
    # Test edge cases
    empty_arr = []
    sort(empty_arr, randomized=False)
    print("Empty array:", empty_arr)
    
    single_element = [42]
    sort(single_element, randomized=True)
    print("Single element:", single_element)
