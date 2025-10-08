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
    
    def postorder_traversal_iterative(self, root):
        """
        Iterative postorder traversal using stack: Left -> Right -> Root
        Visits and prints each node in postorder sequence
        """
        if root is None:
            return
        
        stack = []
        last_visited = None
        current = root
        
        while stack or current:
            if current:
                # Go to the leftmost node
                stack.append(current)
                current = current.left
            else:
                # Peek at the node on top of stack
                peek_node = stack[-1]
                
                # If right child exists and hasn't been processed yet
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    # Process the node
                    print(peek_node.value, end=" ")
                    last_visited = stack.pop()

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
    """
    Simple function to visit a single node by printing its value
    """
    if node is not None:
        print(f"Visiting node with value: {node.value}")

def iterative_visit_all_nodes(root):
    """
    Iteratively visit all nodes in the tree (postorder style) using stack
    """
    if root is None:
        return
    
    stack = []
    last_visited = None
    current = root
    
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                visit_node(peek_node)
                last_visited = stack.pop()

def main():
    tree = create_sample_tree()
    print("Postorder Traversal (Iterative using Stack):")
    print("Order: Left -> Right -> Root")
    tree.postorder_traversal_iterative(tree.root)
    print()  # New line after traversal
    
    print("\nDetailed node visiting:")
    iterative_visit_all_nodes(tree.root)
    
if __name__ == "__main__":
    main()