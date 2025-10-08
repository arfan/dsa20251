from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_tree(node, level=0, prefix=""):
    if node is None:
        return
    
    # Print current node
    print("  " * level + prefix + str(node.data))
    
    if node.left is not None:
        print_tree(node.left, level + 1, "left: ")
    if node.right is not None:
        print_tree(node.right, level + 1, "right: ")
    
def insert_node(root, value):
    # If root is NULL, create new root
    if root is None:
        root = Node(value)
        return root
    
    # Use queue for level-order traversal (mechanism to go level by level)
    queue = deque([root])
    
    # For each level in tree
    while queue:
        # For each node in level
        node = queue.popleft() # dequeue

        # Check if left child is NULL
        if node.left is None:
            node.left = Node(value)
            return root
        
        # Check if right child is NULL
        if node.right is None:
            node.right = Node(value)
            return root
        
        # Add children to queue for next level processing
        queue.append(node.left)
        queue.append(node.right)
    
    return root

# Test the insertNode function
if __name__ == "__main__":
    # Start with empty tree
    root = None
    root = insert_node(root, 10)
    root = insert_node(root, 12)
    root = insert_node(root, 15)
    root = insert_node(root, 25)
    root = insert_node(root, 30)
    root = insert_node(root, 36)

    print_tree(root)
    
    