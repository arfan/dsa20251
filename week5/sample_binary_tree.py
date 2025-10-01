class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree(node, level=0, prefix=""):
    if node is None:
        return
    
    # Print current node
    print("  " * level + prefix + str(node.value))
    
    if node.left is not None:
        print_tree(node.left, level + 1, "└── ")
    if node.right is not None:
        print_tree(node.right, level + 1, "└── ")
    
        
a = Node(4)
b = Node(3)
c = Node(6)

root = a
a.left = b
a.right = c

print_tree(root)