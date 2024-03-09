class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
class DoublyLinkedList:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        if self.start is None:
            n=Node(None,data,None)
            self.start = n
        else:
            n=Node(None,data,self.start)
            self.start = n
    def insert_at_last(self,data):
        
        if self.start is None:
            n = Node(None,data,None)
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n = Node(temp,data,None)
            temp.next = n
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n
    def search(self,data):
        if self.is_empty():
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item is data:
                    return temp
                temp = temp.next
        print("Not found!")
    def printList(self):
        temp = self.start
        while temp is not None:
            print(temp.item)
            temp = temp.next
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next = None
    def delete_item(self, data):
        if self.is_empty():
            pass
        elif self.start.next is None:
            if self.start is data:
                self.start = None
        else:
            temp = self.start
            if temp.item is data:
                temp.next.prev = None
                self.start = temp.next
            else:
                while temp is not None:
                    if temp.item is data:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.next

myList = DoublyLinkedList()
myList.insert_at_start(12)
myList.insert_at_start(13)
myList.insert_at_start(14)
myList.insert_at_last(34)
myList.printList()

    