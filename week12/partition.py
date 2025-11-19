
def partition(a, low, high):
    pivot = a[high]
    i = low
    for j in range(low, high):
        if a[j] > pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    # place pivot in its final position
    a[i], a[high] = a[high], a[i]
    return i


arr = [1, 4, 2, 3]

partition(arr, 0, 3)

print(arr)