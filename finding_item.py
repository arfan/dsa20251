sorted_list = [2, 4, 6, 8, 10, 12, 14, 16]

def find_element(arr, item, left, right):
    if left > right:
        return -1
    
    mid = (left+right) // 2

    if arr[mid] < item:
        return find_element(arr, item, mid+1, right)
    elif arr[mid] > item:
        return find_element(arr, item, left, mid-1)
    else:
        return mid

result = find_element(sorted_list, 2, 0, len(sorted_list)-1)
print(result)