class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return f"Node({self.value})"

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def inorder_traversal_iterative(self, root):
        if root is None:
            return
        
        stack = []
        current = root
        
        # Process nodes until both stack is empty and current is None
        while stack or current:
            # Go to the leftmost node of the current node
            if current:
                stack.append(current)
                current = current.left
            else:
                # Current must be None at this point
                # Pop the top item from stack and print it
                current = stack.pop()
                print(current.value, end=" ")
                
                # We have visited the node and its left subtree, now visit right subtree
                current = current.right

def create_sample_tree():
    tree = BinaryTree()
    
    # Create nodes
    tree.root = TreeNode(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    tree.root.right.left = TreeNode(6)
    tree.root.right.right = TreeNode(7)
    
    return tree

def visit_node(node):
    if node is not None:
        print(f"Visiting node with value: {node.value}")

def iterative_visit_all_nodes(root):
    if root is None:
        return
    
    stack = []
    current = root
    
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            visit_node(current)
            current = current.right

def main():
    tree = create_sample_tree()
    print("Inorder Traversal (Iterative using Stack):")
    print("Order: Left -> Root -> Right")
    tree.inorder_traversal_iterative(tree.root)
    print()  # New line after traversal
    
    print("\nDetailed node visiting:")
    iterative_visit_all_nodes(tree.root)
    
if __name__ == "__main__":
    main()