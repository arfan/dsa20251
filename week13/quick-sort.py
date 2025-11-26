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


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]

    arr = sample.copy()
    quick_sort(arr, 0, len(arr)-1)
    print("Quick Sort:", arr)