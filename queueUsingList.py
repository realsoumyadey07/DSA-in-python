class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items)
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("Stack is underflow")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Stack is underflow")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is underflow")
    def size(self):
        return len(self.items)