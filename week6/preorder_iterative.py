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
    
    def preorder_traversal_iterative(self, root):
        if root is None:
            return
        
        # Create a stack and push the root node
        stack = []

        # Push the root
        stack.append(root)
        
        # Process nodes until stack is empty
        while stack:
            # Pop a node from stack and print it
            current = stack.pop()
            print(current.value, end=" ") # Visit the current
            
            # Push right child first (so left is processed first)
            if current.right:
                stack.append(current.right)
            
            # Push left child
            if current.left:
                stack.append(current.left)

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
    
    stack = [root]
    
    while stack:
        current = stack.pop()
        visit_node(current)
        
        # Push right child first (so left is processed first)
        if current.right:
            stack.append(current.right)
        
        if current.left:
            stack.append(current.left)

def main():
    tree = create_sample_tree()
    print("Preorder Traversal (Iterative using Stack):")
    print("Order: Root -> Left -> Right")
    tree.preorder_traversal_iterative(tree.root)
    print()  # New line after traversal
    
    print("\nDetailed node visiting:")
    iterative_visit_all_nodes(tree.root)
    
if __name__ == "__main__":
    main()