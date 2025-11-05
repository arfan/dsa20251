class PriorityQueue:
    def __init__(self):
        # Each element is a tuple (priority, value)
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def _parent(self, index):
        return (index - 1) // 2 if index > 0 else None

    def _left_child(self, index):
        left = 2 * index + 1
        return left if left < len(self.heap) else None

    def _right_child(self, index):
        right = 2 * index + 2
        return right if right < len(self.heap) else None

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _percolate_up(self, index):
        print("percolate_up")
        """Move the element at index up until heap property is restored."""
        parent = self._parent(index)
        while parent is not None and self.heap[index][0] < self.heap[parent][0]:
            self._swap(index, parent)
            index = parent
            parent = self._parent(index)

    def _percolate_down(self, index):
        """Move the element at index down until heap property is restored."""
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            smallest = index

            if left is not None and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right is not None and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == index:
                break

            self._swap(index, smallest)
            index = smallest

    def insert(self, item, priority):
        """Insert an item with given priority into the heap."""
        self.heap.append((priority, item))
        self._percolate_up(len(self.heap) - 1)

    def extract_min(self):
        """Remove and return the item with the smallest priority."""
        if not self.heap:
            raise IndexError("extract_min from empty heap")

        min_item = self.heap[0]
        last_item = self.heap.pop()

        if self.heap:  # if not empty after pop
            self.heap[0] = last_item
            self._percolate_down(0)

        return min_item[1], min_item[0]

    def peek(self):
        """Return the item with the smallest priority without removing it."""
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0][1], self.heap[0][0]

    def __repr__(self):
        return "Heap: [" + ", ".join(f"{v}:{p}" for p, v in self.heap) + "]"

    def print_tree(self, index=0, prefix="", is_left=None):
        """Print the heap as a tree structure."""
        if index >= len(self.heap):
            return
        
        priority, value = self.heap[index]
        
        # Print current node
        if is_left is None:
            print(f"{prefix}Root: {value}:{priority}")
        else:
            connector = "├── L: " if is_left else "└── R: "
            print(f"{prefix}{connector}{value}:{priority}")
        
        # Print children
        left = self._left_child(index)
        right = self._right_child(index)
        
        if left is not None or right is not None:
            if left is not None:
                extension = "│   " if right is not None else "    "
                self.print_tree(left, prefix + extension, True)
            if right is not None:
                self.print_tree(right, prefix + "    ", False)

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert('a', 5)
    pq.insert('b', 9)
    pq.insert('c', 12)
    pq.insert('d', 13)
    pq.insert('e', 16)
    pq.insert('f', 45)

    print(pq)  # view heap structure
    
    print("\nHeap as tree:")
    pq.print_tree()

    pq.insert('g', 2)
    pq.print_tree()
