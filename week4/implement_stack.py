class StackSample:
    def __init__(self, element):
        self.size = element
        self.data = [0] * element # [0,0,0,0,0] if element is 5
        self.top = -1

    def push(self, el):
        if self.top == self.size - 1:
            print("exception stack overflow")
            return None

        self.top = self.top+1
        self.data[self.top] = el

    def pop(self):
        if self.top < 0:
            print("exception empty stack")
            return None
        
        value = self.data[self.top]
        self.top = self.top - 1

        return value

    def print(self):
        print("content=", self.data, " top=", self.top)

    def isEmpty(self):
        return self.top == -1
    
    def peek(self):
        return self.data[self.top]


stack = StackSample(10)

stack.push(5)
print("isEmpty=", stack.isEmpty())
print("peek", stack.peek())
stack.print()

