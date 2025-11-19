import random
from typing import List

# -------------------------
# MergeSort (in-place)
# -------------------------
def merge(left: List[int], right: List[int], out: List[int]) -> None:
    """
    Merges two sorted lists `left` and `right` into `out`.
    """
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            out[k] = left[i]
            i += 1
        else:
            out[k] = right[j]
            j += 1
        k += 1
    # copy any remaining
    while i < len(left):
        out[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        out[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr: List[int]) -> None:
    """
    Sorts list `arr` in-place using merge sort.
    """
    n = len(arr)
    if n <= 1: # if array has 0 or 1 element
        return

    mid = n // 2 #integer division
    left = arr[:mid]
    right = arr[mid:]
    # recursively sort halves
    merge_sort(left)
    merge_sort(right)
    # merge back into arr
    merge(left, right, arr)


# -------------------------
# Sample Usage
# -------------------------
if __name__ == "__main__":
    arr = [1, 4, 2, 3, 8]
    merge_sort(arr)
    print(arr)
