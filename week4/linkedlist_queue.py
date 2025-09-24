class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, element):
        new_node = Node(element)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        # Create a new Node with data as item
        # If front is None:
        #     Set front and rear to the new Node
        # Else:
        #     Set the next of rear to the new Node
        #     Set rear to the new Node


    def dequeue(self):
        # If front is None:
        #     Print "Queue is empty. Cannot dequeue."
        #     Return None or a sentinel value indicating an error
        # Get data from front Node
        # Set front to the next Node
        # If front is now None:
        #     Set rear to None
        # Return data
        if self.front is None:
            print("Queue is empty. Cannot dequeue.")
            return None
        
        result_data = self.front.value  # Fixed: use 'value' instead of 'data'
        self.front = self.front.next
        
        # If front becomes None after dequeue, set rear to None too
        if self.front is None:
            self.rear = None
            
        return result_data

    def print(self):
        if self.front is None:
            print("empty queue")
            return

        curr = self.front
        print("elements: [", end=" ")
        while curr != None:
            print(curr.value, end=" ")
            curr = curr.next
        print("]")
        
ll = LinkedList()

ll.enqueue(1)
ll.print()

ll.enqueue(3)
ll.print()

result = ll.dequeue()
print(result)
ll.print()
