class Stack(list):
    def is_empty(self):
        return len(self) == 0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        if not self.is_empty():
            return len(self)
        else:
            raise IndexError("Stack is empty")

myList = Stack()
myList.push(34)
myList.push(23)
myList.push(56)