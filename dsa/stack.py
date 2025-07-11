class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.stack.pop()

    def push(self, element):
        self.stack.append(element)

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.stack[-1]

    def printStack(self):
        print(self.stack)

new_stack = Stack()
print(new_stack.isEmpty())
new_stack.push(9)
print("stack: ", end="")
new_stack.printStack()