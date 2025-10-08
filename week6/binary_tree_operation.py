class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    
    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)
    
    def _delete_recursive(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.data = successor.data
                node.right = self._delete_recursive(node.right, successor.data)
        return node
    
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
            return
        self._print_tree_recursive(self.root, "", "Root")
    
    def _print_tree_recursive(self, node, prefix, position):
        if node is not None:
            print(f"{prefix}{position}: {node.data}")
            if node.left is not None or node.right is not None:
                if node.left is not None:
                    self._print_tree_recursive(node.left, prefix + "  ", "L")
                else:
                    print(f"{prefix}  L: None")
                if node.right is not None:
                    self._print_tree_recursive(node.right, prefix + "  ", "R")
                else:
                    print(f"{prefix}  R: None")


def main():
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    
    bst.print_tree()
    bst.delete(1)
    bst.print_tree()

if __name__ == "__main__":
    main()
