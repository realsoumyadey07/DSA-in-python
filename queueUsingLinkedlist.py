class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    def is_empty(self):
        return self.item_count is 0
    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        elif self.front is self.rear:
            self.front = None
            self.rear = None
            self.item_count-=1
        else:
            self.front = self.front.next
            self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError('Stack underflow')
        else:
            return self.front.data
    def get_rear(self):
        if self.is_empty():
            raise IndexError('Stack underflow')
        else:
            return self.rear.data
        
    def size(self):
        return self.item_count
    
        