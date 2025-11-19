import random
from typing import List


def partition(a: List[int], low: int, high: int) -> int:
    """
    Partitions array around pivot (last element).
    Moves elements greater than pivot to the left.
    Returns the final position of the pivot.
    """
    # pivot as last element (we'll move greater-than-pivot to left)
    pivot = a[high]
    i = low
    for j in range(low, high):
        if a[j] > pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    # place pivot in its final position
    a[i], a[high] = a[high], a[i]
    return i


def quickselect(a: List[int], low: int, high: int, k: int) -> int:
    """
    Finds the k-th largest element in array `a` between indices low and high.
    k is the rank among largest: 1 means largest, 2 means second largest, etc.
    """
    # k is the rank among largest: 1 means largest, etc.
    if low == high:
        return a[low]

    # optional: pick a random pivot by swapping a random element with a[high]
    pivot_idx = random.randrange(low, high + 1)
    a[pivot_idx], a[high] = a[high], a[pivot_idx]

    pivot_index = partition(a, low, high)
    size_of_right = high - pivot_index + 1  # number of elements >= pivot to the right (including pivot)

    if size_of_right == k:
        return a[pivot_index]
    elif size_of_right > k:
        # k-th largest is in right partition
        return quickselect(a, pivot_index + 1, high, k)
    else:
        # k-th largest is in left partition; adjust k
        return quickselect(a, low, pivot_index - 1, k - size_of_right)


def kth_largest(nums: List[int], k: int) -> int:
    """
    Returns the k-th largest element in nums (1-based k).
    Raises ValueError if k is out of bounds.
    """
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and len(nums)")

    def partition(a: List[int], low: int, high: int) -> int:
        # pivot as last element (we'll move greater-than-pivot to left)
        pivot = a[high]
        i = low
        for j in range(low, high):
            if a[j] > pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        # place pivot in its final position
        a[i], a[high] = a[high], a[i]
        return i

    def quickselect(a: List[int], low: int, high: int, k: int) -> int:
        # k is the rank among largest: 1 means largest, etc.
        if low == high:
            return a[low]

        # optional: pick a random pivot by swapping a random element with a[high]
        pivot_idx = random.randrange(low, high + 1)
        a[pivot_idx], a[high] = a[high], a[pivot_idx]

        pivot_index = partition(a, low, high)
        size_of_right = high - pivot_index + 1  # number of elements >= pivot to the right (including pivot)

        if size_of_right == k:
            return a[pivot_index]
        elif size_of_right > k:
            # k-th largest is in right partition
            return quickselect(a, pivot_index + 1, high, k)
        else:
            # k-th largest is in left partition; adjust k
            return quickselect(a, low, pivot_index - 1, k - size_of_right)

    # operate on a copy to avoid modifying original list (optional)
    arr_copy = nums[:] 
    return quickselect(arr_copy, 0, len(arr_copy) - 1, k)