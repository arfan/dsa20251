class DynamicArrayStack:
    """
    A stack implementation using a dynamic array that simulates memory allocation.
    The array starts with a fixed capacity and doubles when it runs out of space.
    Follows the LIFO (Last In, First Out) principle.
    """
    
    def __init__(self, initial_capacity=2):
        """
        Initialize the stack object with top index and fixed capacity array.
        
        Args:
            initial_capacity (int): Initial size of the array (default: 2)
        """
        self.top = -1
        self.capacity = initial_capacity
        self.array = [None] * self.capacity  # Fixed-size array filled with None
        self.actual_size = 0  # Track actual number of elements
    
    def isEmpty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
        """
        return self.top == -1
    
    def getSize(self):
        """
        Get the current size of the stack.
        
        Returns:
            int: Number of elements in the stack
        """
        if self.isEmpty():
            return 0
        return self.actual_size
    
    def _resize_array(self):
        """
        Resize the array by doubling its capacity when it's full.
        This simulates dynamic memory allocation.
        """
        old_capacity = self.capacity
        new_capacity = self.capacity * 2
        
        print(f"📈 Array is full! Resizing from {old_capacity} to {new_capacity}")
        
        # Create new array with double capacity
        new_array = [None] * new_capacity
        
        # Copy existing elements to new array
        for i in range(self.actual_size):
            new_array[i] = self.array[i]
        
        # Update array and capacity
        self.array = new_array
        self.capacity = new_capacity
        
        print(f"✅ Array resized successfully! New capacity: {self.capacity}")
    
    def push(self, item):
        """
        Push an item onto the top of the stack.
        Resizes array if capacity is exceeded.
        
        Args:
            item: The item to be pushed onto the stack
        """
        # Check if we need to resize
        if self.actual_size >= self.capacity:
            self._resize_array()
        
        self.top += 1
        self.actual_size += 1
        self.array[self.top] = item
        
        print(f"Pushed: {item} (Size: {self.actual_size}/{self.capacity})")
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack, or None if stack is empty
        """
        if self.isEmpty():
            print("Stack is empty. Cannot pop.")
            return None
        
        item = self.array[self.top]  # Get the top element
        self.array[self.top] = None  # Clear the slot
        self.top -= 1
        self.actual_size -= 1
        
        print(f"Popped: {item} (Size: {self.actual_size}/{self.capacity})")
        return item
    
    def peek(self):
        """
        Return the top item from the stack without removing it.
        
        Returns:
            The top item from the stack, or None if stack is empty
        """
        if self.isEmpty():
            print("Stack is empty. Cannot peek.")
            return None
        
        return self.array[self.top]  # Return the top element
    
    def display(self):
        """
        Display the current contents of the stack and array status.
        """
        if self.isEmpty():
            print("Stack is empty")
        else:
            # Show only the actual elements (excluding None values)
            actual_elements = [self.array[i] for i in range(self.actual_size)]
            print(f"Stack contents (top to bottom): {actual_elements[::-1]}")
        
        print(f"Array capacity: {self.capacity}")
        print(f"Actual size: {self.actual_size}")
        print(f"Top index: {self.top}")
        print(f"Full array view: {self.array}")
        print("-" * 50)


# Example usage and testing
if __name__ == "__main__":
    # Create a new stack with initial capacity of 2
    print("🚀 Creating DynamicArrayStack with initial capacity of 2")
    stack = DynamicArrayStack(initial_capacity=2)
    stack.display()
    
    # Test isEmpty on empty stack
    print(f"\nIs stack empty? {stack.isEmpty()}")
    print(f"Stack size: {stack.getSize()}")
    
    # Test pop and peek on empty stack
    print("\n🔍 Testing pop and peek on empty stack:")
    stack.pop()
    stack.peek()
    
    # Push items to demonstrate dynamic resizing
    print("\n📚 Pushing items to demonstrate dynamic resizing:")
    print("Pushing item: 10")
    stack.push(10)
    stack.display()
    
    print("Pushing item: 20")
    stack.push(20)
    stack.display()
    
    print("Pushing item: 30 (This should trigger resize!)")
    stack.push(30)
    stack.display()
    
    print("Pushing item: 40")
    stack.push(40)
    stack.display()
    
    print("Pushing item: 50 (This should trigger another resize!)")
    stack.push(50)
    stack.display()
    
    # Test peek
    print(f"🔍 Peek (top element): {stack.peek()}")
    
    # Test multiple pops
    print("\n⬇️ Testing multiple pops:")
    while not stack.isEmpty():
        stack.pop()
        if not stack.isEmpty():
            stack.display()
    
    # Final state
    print("\n🏁 Final state:")
    stack.display()
    print(f"Is stack empty? {stack.isEmpty()}")