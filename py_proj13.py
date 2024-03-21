class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.top = -1
        self.list = []

    def __str__(self):
        values = self.list[::-1]
        values = [str(x) for x in values]
        return '\n'.join(values)

    def push(self, value):
        if self.top == self.maxsize - 1:
            print("The Stack is full")
        else:
            self.list.append(value)
            self.top += 1
            print(value, "has been successfully added to the stack")

    def pop(self):
        if self.top == -1:
            print("The Stack is Empty")
        else:
            print("Popped item =", self.list.pop())
            self.top -= 1

    def display(self):
        if self.top == -1:
            print("The stack is empty")
        else:
            print("Contents of the stack are:")
            print(self)

tempstack = Stack(3)
tempstack.push(10)
tempstack.push(20)
tempstack.push(30)
tempstack.display()
tempstack.pop()
tempstack.display()