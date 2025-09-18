class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    

def print_linkedlist(h):
    curr = h
    while curr != None:
        print(curr.value)
        curr = curr.next

node4 = Node(4, None)
node3 = Node(17, node4)
node2 = Node(1, node3)
node1 = Node(5, node2)

head:Node = node1

# first time after creating
print_linkedlist(head)

temp = head
head = head.next
# free(temp)

# after inserting to first element
print("after deleting the first element")
print_linkedlist(head)
