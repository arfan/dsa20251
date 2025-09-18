class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    

def print_linkedlist(h):
    curr = h
    while curr != None:
        print(curr.value)
        curr = curr.next


node3 = Node(7, None)
node2 = Node(15, node3)
node1 = Node(4, node2)

head:Node = node1

print_linkedlist(head)


new_node = Node(40, None)
# start insert new_node to last node
last_node = head
while(last_node.next != None):
    last_node = last_node.next
print("value of last node", last_node.value)

last_node.next = new_node
# end of process

# after inserting to last node
print("after inserting")
print_linkedlist(head)
