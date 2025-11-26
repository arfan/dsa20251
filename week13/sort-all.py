# ============================================
# Sorting & Searching Algorithms
# From Week 13 - Data Structure & Algorithm
# ============================================

# -------------------------
# 1. Bubble Sort
# -------------------------
def bubble_sort(A):
    n = len(A)
    while True:
        swapped = False
        for i in range(1, n):
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]
                swapped = True
        n -= 1
        if not swapped:
            break
    return A


# -------------------------
# 2. Selection Sort
# -------------------------
def selection_sort(A):
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A


# -------------------------
# 3. Quick Sort + Partition
# -------------------------
def partition(A, low, high):
    pivot = A[high]
    i = low
    for j in range(low, high):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[high] = A[high], A[i]
    return i


def quick_sort(A, low, high):
    if low < high:
        pivot_index = partition(A, low, high)
        quick_sort(A, low, pivot_index - 1)
        quick_sort(A, pivot_index + 1, high)
    return A


# -------------------------
# 4. Merge Sort + Merge
# -------------------------
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)


# -------------------------
# 5. Insertion Sort
# -------------------------
def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A


# -------------------------
# 6. Unordered Linear Search
# -------------------------
def unordered_linear_search(A, target):
    for i in range(len(A)):
        if A[i] == target:
            return i
    return None  # Not found


# -------------------------
# 7. Ordered Linear Search
# -------------------------
def ordered_linear_search(A, target):
    for i in range(len(A)):
        if A[i] == target:
            return i
        elif A[i] > target:
            return None
    return None


# -------------------------
# 8. Binary Search
# -------------------------
def binary_search(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] == target:
            return mid
        elif A[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


# -------------------------
# Testing Section (Optional)
# -------------------------
if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]

    print("Bubble Sort:", bubble_sort(sample.copy()))
    print("Selection Sort:", selection_sort(sample.copy()))
    print("Insertion Sort:", insertion_sort(sample.copy()))
    print("Merge Sort:", merge_sort(sample.copy()))

    arr = sample.copy()
    quick_sort(arr, 0, len(arr)-1)
    print("Quick Sort:", arr)

    print("Unordered Linear Search (find 9):", unordered_linear_search(sample, 9))
    print("Ordered Linear Search (sorted list):", ordered_linear_search(sorted(sample), 5))
    print("Binary Search (sorted list):", binary_search(sorted(sample), 6))