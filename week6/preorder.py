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
    
    def preorder_traversal(self, node):
        """
        Recursive preorder traversal: Root -> Left -> Right
        Visits and prints each node in preorder sequence
        """
        if node is not None:
            print(node.value, end=" ")  # Visit root
            self.preorder_traversal(node.left)   # Traverse left subtree
            self.preorder_traversal(node.right) # Traverse right subtree

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

def recursive_visit_all_nodes(node):
    """
    Recursively visit all nodes in the tree (preorder style)
    """
    if node is not None:
        visit_node(node)                        # Visit current node
        recursive_visit_all_nodes(node.left)   # Visit left subtree
        recursive_visit_all_nodes(node.right)  # Visit right subtree

def main():    
    tree = create_sample_tree()
    print("Preorder Traversal (Root -> Left -> Right):")
    tree.preorder_traversal(tree.root)
    print()  # New line after traversal

if __name__ == "__main__":
    main()
