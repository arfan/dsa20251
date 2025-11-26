if __name__ == "__main__":
    arr = [1, 2, 5, 6, 9]

    length = len(arr)
    target = 3

    low = 0
    high = 4
    found = False

    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == target:
            print("target location =", mid)
            found = True
            break
        elif arr[mid] < target:
            low = mid+1
        elif arr[mid] > target:
            high = mid - 1

    if not found:
        print("target not found")