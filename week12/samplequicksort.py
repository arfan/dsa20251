
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

def quicksort_process(arr, low, high):
    if low >= high:
        return
    
    pivot_index = partition(arr, low, high)
    print("pivot_index=", pivot_index)
    print("arr", arr)

    quicksort_process(arr, low, pivot_index-1)
    quicksort_process(arr, pivot_index+1, high)
    

def quicksort(arr):
    quicksort_process(arr, 0, len(arr) - 1)

arr = [5, 2, 4, 1, 3]
quicksort(arr)

print(arr)