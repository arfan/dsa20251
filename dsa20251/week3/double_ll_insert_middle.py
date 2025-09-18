class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev # left pointer
        self.next = next # right pointer
    

def print_linkedlist(h):
    curr = h
    while curr != None:
        print(curr.value)
        curr = curr.next


node4 = Node(40)
node3 = Node(7)
node2 = Node(15)
node1 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

node4.prev = node3
node3.prev = node2
node2.prev = node1

head = node1

print("print original linkedlist")
print_linkedlist(head)

new_node = Node(300)
new_node.next = node2.next
new_node.prev = node2
node2.next = new_node
new_node.next.prev = new_node

print("print after insert to middle of linkedlist")
print_linkedlist(head)
