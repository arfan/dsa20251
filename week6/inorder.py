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
    
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)   # Traverse left subtree
            print(node.value, end=" ")  # Visit root
            self.inorder_traversal(node.right) # Traverse right subtree

def create_sample_tree():
    tree = BinaryTree()
    
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    
    # Create nodes
    tree.root = node_1
    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5
    node_3.left = node_6
    node_3.right = node_7

    return tree

def main():    
    tree = create_sample_tree()
    print("Inorder Traversal (Left -> Root -> Right):")
    tree.inorder_traversal(tree.root)
    print()  # New line after traversal

if __name__ == "__main__":
    main()
