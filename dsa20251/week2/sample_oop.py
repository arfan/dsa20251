class Person:
    def __init__(self, name, age):
        self.name = name    # property
        self.age = age      # property

    def greet(self):        # method
        print("Hello, my name is", self.name, "my age is", self.age)

p1 = Person("Arfan", 25)
p1.greet()   # Hello, my name is Arfan, my age is 25
