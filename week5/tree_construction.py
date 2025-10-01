class Node:
    """A node class for tree structure"""
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        """Add a child node to this node's children list"""
        self.children.append(child_node)
    
    def __str__(self):
        return f"Node({self.value})"
    
    def __repr__(self):
        return self.__str__()


def initialize_node(value):
    """Initialize a new node with the given value"""
    node = Node(value)
    return node


def construct_tree():
    # Initialize root node
    root_node = initialize_node("Root")
    
    # Create first level children
    child1 = initialize_node("Child1")
    child2 = initialize_node("Child2")
    
    # Add children to root
    root_node.add_child(child1)
    root_node.add_child(child2)
    
    # Create second level children for child1
    child1_1 = initialize_node("Child1_1")
    child1.add_child(child1_1)
    
    # Create second level children for child2
    child2_1 = initialize_node("Child2_1")
    child2_2 = initialize_node("Child2_2")
    child2.add_child(child2_1)
    child2.add_child(child2_2)
    
    return root_node


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


# def traverse_tree_preorder(node, result=None):
#     if result is None:
#         result = []
    
#     if node is not None:
#         result.append(node.value)
#         for child in node.children:
#             traverse_tree_preorder(child, result)
    
#     return result


def main():
    """Main function to demonstrate the tree construction"""
    print("Constructing tree based on pseudocode algorithm...")
    print("=" * 50)
    
    # Construct the tree
    root = construct_tree()
    
    # Display the tree structure
    print("Tree Structure:")
    print_tree(root)
    
    # print("\nPre-order Traversal:")
    # traversal_result = traverse_tree_preorder(root)
    # print(" -> ".join(traversal_result))
    
    # print("\nTree Construction Complete!")


if __name__ == "__main__":
    main()
