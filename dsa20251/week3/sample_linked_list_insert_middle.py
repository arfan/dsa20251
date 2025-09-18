class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    

def print_linkedlist(h):
    curr = h
    while curr != None:
        print(curr.value)
        curr = curr.next

node4 = Node(40, None)
node3 = Node(7, node4)
node2 = Node(15, node3)
node1 = Node(4, node2)

head:Node = node1

# first time after creating
print("first time after creating")
print_linkedlist(head)


new_node = Node(500, Node)

new_node.next = node2.next
node2.next = new_node

# after inserting  element
print("after inserting")
print_linkedlist(head)
