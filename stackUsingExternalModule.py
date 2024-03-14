from singlyLinkedList import *

class Stack:
    def __init__(self):
        self.myList = SLL()
        self.item_count = 0
    def is_empty(self):
        return self.myList.isEmpty()
    def push(self, data):
        self.myList.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.myList.delete_first()
            self.item_count-=1
    def peek(self):
        if not self.myList.isEmpty():
            return self.myList.start
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return self.item_count

            