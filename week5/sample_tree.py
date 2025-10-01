class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def print_tree(node, level=0, prefix=""):
    if node is None:
        return
    
    # Print current node
    print("  " * level + prefix + str(node.value))
    
    # Print children
    for i, child in enumerate(node.children):
        if i == len(node.children) - 1:
            print_tree(child, level + 1, "└── ")
        else:
            print_tree(child, level + 1, "├── ")

a = Node(2)
b = Node(3)
c = Node(4)

root = a
a.children.append(b)
a.children.append(c)

print_tree(root)