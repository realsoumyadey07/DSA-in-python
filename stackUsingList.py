class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) is 0
    def push(self,data):
        self.items.push(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self.items)