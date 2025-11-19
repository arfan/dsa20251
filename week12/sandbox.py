#splitting an array

arr = [4, 2, 3, 1]
n = len(arr)
mid = n // 2 #integer division
left = arr[:mid]
right = arr[mid:]

print("left", left)
print("right", right)

