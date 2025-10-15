
def index_finder(arr, N):
    for i in range(len(arr)):  # done len(arr) times 
        for j in range(len(arr)): # done len(arr) times 
            print(i, j)
            if i != j:
                if arr[i]+arr[j] == N:
                    return i, j

    return -1, -1

# i, j = index_finder([4, 1, 3, 6, 7], 10)
# print("i=", i,"j=", j)

def binary_search(arr, N, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    # Base case: element not found
    if left > right:
        return -1
    
    middle = (left + right) // 2
    
    if arr[middle] == N:
        return middle
    elif arr[middle] < N:
        # Search right half
        return binary_search(arr, N, middle + 1, right)
    else:
        # Search left half
        return binary_search(arr, N, left, middle - 1)

arr = [1, 3, 4, 6, 7]
N = 6
result = binary_search(arr, N)
print(f"Searching for {N} in {arr}: index = {result}")

# Test with different values
test_values = [1, 3, 4, 6, 7, 0, 5, 8]
for val in test_values:
    idx = binary_search(arr, val)
    print(f"Searching for {val}: index = {idx}")


# Head -> Node1 -> Node2 -> Node3
# Head -> Node3 -> Node2 -> Node1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a singly linked list iteratively.
    
    Args:
        head: The head node of the linked list
        
    Returns:
        The new head of the reversed linked list
    """
    prev = None
    current = head
    
    while current is not None:
        # Store the next node
        next_temp = current.next
        # Reverse the link
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_temp
    
    # prev is now the new head of the reversed list
    return prev

# Test the reverse_linked_list function
def print_linked_list(head):
    """Helper function to print the linked list"""
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values)

# Create a test linked list: 1 -> 2 -> 3 -> 4
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:", print_linked_list(node1))

# Reverse the list
reversed_head = reverse_linked_list(node1)
print("Reversed list:", print_linked_list(reversed_head))
