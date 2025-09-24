class StackSample:
    def __init__(self, element):
        self.size = element
        self.data = [0] * element # [0,0,0,0,0] if element is 5
        self.top = -1

    def push(self, el):
        if self.top == self.size - 1:
            print("exception full stack")
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


stack = StackSample(5)

stack.print()
value = stack.pop()

print(value)

stack.push("T")
stack.push("A")

stack.print()
result = stack.pop()
print(result)

# stack.push(1)
# stack.print()

# stack.push(2)
# stack.print()

# stack.push(3)
# stack.print()

# stack.push(4)
# stack.print()

# stack.push(5)
# stack.print()

# stack.push(6)
# stack.print()
