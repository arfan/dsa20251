from collections import deque

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
    
    def level_order_traversal(self, root):
        if root is None:
            return
        
        # Create a queue and add the root node
        queue = deque([root])
        
        while queue:
            # Remove node from front of queue and print it
            current = queue.popleft()
            print(current.value, end=" ")
            
            # Add left child to queue
            if current.left:
                queue.append(current.left)
            
            # Add right child to queue
            if current.right:
                queue.append(current.right)
    
    def level_order_traversal_with_levels(self, root):
        """
        Level-by-level traversal showing each level separately
        """
        if root is None:
            return
        
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            print(f"Level {level}: ", end="")
            
            # Process all nodes at current level
            for _ in range(level_size):
                current = queue.popleft()
                print(current.value, end=" ")
                
                # Add children for next level
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            print()  # New line after each level
            level += 1
    
    def level_order_traversal_right_to_left(self, root):
        if root is None:
            return
        
        queue = deque([root])
        
        while queue:
            current = queue.popleft()
            print(current.value, end=" ")
            
            # Add right child first, then left child
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)

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

def level_order_visit_all_nodes(root):
    if root is None:
        return
    
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        visit_node(current)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def get_tree_height(root):
    if root is None:
        return 0
    
    queue = deque([root])
    height = 0
    
    while queue:
        height += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            current = queue.popleft()
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    
    return height

def main():
    tree = create_sample_tree()
    
    print("1. Level Order Traversal (using Queue):")
    print("Order: Level by level, left to right")
    tree.level_order_traversal(tree.root)
    print()
    print()
    
    print("2. Level Order Traversal with Level Numbers:")
    tree.level_order_traversal_with_levels(tree.root)
    print()
    
    print("3. Level Order Traversal (Right to Left):")
    tree.level_order_traversal_right_to_left(tree.root)
    print()
    print()
    
    print("4. Tree Height:", get_tree_height(tree.root))
    print()
    
    print("5. Detailed node visiting (level by level):")
    level_order_visit_all_nodes(tree.root)
    
if __name__ == "__main__":
    main()