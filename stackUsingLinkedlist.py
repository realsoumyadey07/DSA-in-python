class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self):
        self.top = None
        self.item_count = 0
    def is_empty(self):
        return self.item_count is 0
    def push(self,data):
        n = Node(data,self.top)
        self.top = n
        self.item_count += 1
    def pop(self):
        if self.item_count is 0:
            raise IndexError("Stack is empty")
        else:
            self.top = self.top.next
            self.item_count -= 1
    def peek(self):
        if not self.is_empty():
            return self.top.item
        else:
            raise IndexError("Stack is empty")
        
list = Stack()
list.push(32)
list.push(45)
list.push(76)
list.pop()
list.peek()

