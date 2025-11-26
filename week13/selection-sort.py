def selection_sort(A):
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]

    print("Selection Sort:", selection_sort(sample.copy()))