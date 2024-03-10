class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class CLL:
    def __init__(self, last=None):
        self.last = last
    def is_empty(self):
        return self.last is None
    def insert_at_first(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            self.last = n
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n
    def search(self,data):
        if self.is_empty():
            pass
        else:
            temp = self.last
            while temp is not None:
                if temp.item is data:
                    return temp
                temp = temp.next
    def insert_after(self, data, temp):
        if temp is not None:
            n = Node(data,temp.next)
            if temp is self.last:
                self.last = n
    def printList(self):
        if self.last is not None:
            temp = self.last
            while temp.next!=self.last:
                print(temp.item+"->")
                temp =temp.next

