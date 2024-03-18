class PriorityQueue:
    def __init__(self):
        self.items = []
    def push(self, data, priority):
        index = 0
        while index<len(self.items) and self.items[index][1]<priority:
            index+=1
        self.items.insert(index,(data, priority))
    def is_empty(self):
        return len(self.items) is 0
    def pop(self):
        if self.is_empty():
            raise IndexError('Priority Queue is empty')
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)
    















