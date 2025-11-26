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


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]

    print("Bubble Sort:", bubble_sort(sample.copy()))
