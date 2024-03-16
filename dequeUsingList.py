class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items)
    def insert_at_first(self, data):
        self.items.insert(0, data)
    def insert_at_last(self, data):
        self.items.append(data)
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.items.pop(0)
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.items.pop()
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.items[0]
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)
    