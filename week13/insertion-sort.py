def insertion_sort(A):
    for i in range(1, len(A)):
        print(A)
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]

    print("Insertion Sort:", insertion_sort(sample.copy()))