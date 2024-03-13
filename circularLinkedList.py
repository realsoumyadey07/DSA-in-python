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
    def delete_first(self):
        if self.last is None:
            pass
        elif self.last.next is self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next
    def delete_last(self):
        if not self.is_empty():
            if self.last.next is self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next!= self.last:
                    temp = temp.next
                temp.next = self.last.next
    def delete_item(self,data):
        if self.is_empty():
            pass
        else:
            if self.last.next is self.last:
                if self.last.item is data:
                    self.last = None
            else:
                temp = self.last
                j = self.last.next
                while j.next is not self.last:
                    if j.item is data:
                        temp.next = j.next
                        

