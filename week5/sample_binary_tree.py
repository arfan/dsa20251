from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_node(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert_node(root.left, data)
    elif data > root.data:
        root.right = insert_node(root.right, data)

    return root

def print_tree(node, level=0, prefix=""):
    if node is None:
        return
    
    # Print current node
    print("  " * level + prefix + str(node.data))
    
    if node.left is not None:
        print_tree(node.left, level + 1, "left: ")
    if node.right is not None:
        print_tree(node.right, level + 1, "right: ")
    
        
a = Node(4)
root = a

root = insert_node(root, 3)
root = insert_node(root, 5)
root = insert_node(root, 1)

print_tree(root)