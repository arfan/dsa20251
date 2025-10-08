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
    
    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)  # Traverse left subtree
            self.postorder_traversal(node.right) # Traverse right subtree
            print(node.value, end=" ")           # Visit root

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

def recursive_visit_all_nodes(node):
    if node is not None:
        recursive_visit_all_nodes(node.left)   # Visit left subtree
        recursive_visit_all_nodes(node.right)  # Visit right subtree
        visit_node(node)                        # Visit current node

def main():
    
    tree = create_sample_tree()
    print("Postorder Traversal (Left -> Right -> Root):")
    tree.postorder_traversal(tree.root)
    print()  # New line after traversal
    
if __name__ == "__main__":
    main()