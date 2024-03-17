class PriorityQueue:
    def __init__(self):
        self.itemt = []
    def push(self, data, priority):
        index = 0
        while index<len(self.itemt) and self.itemt[index][1]<priority:
            index+=1
        self.itemt.insert(index,(data, priority))
    def is_empty(self):
        return len(self.itemt) is 0
    def pop(self):
        if self.is_empty():
            raise IndexError('Priority Queue is empty')
        return self.itemt.pop(0)[0]
    def size(self):
        return len(self.itemt)
    















