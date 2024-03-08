class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next= next
class SLL:
    def __init__(self, start=None):
        self.start = start
    def isEmpty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = Node(data, self.start)
        self.start = n
    def insert_at_last(self, data):
        n= Node(data)
        if not self.isEmpty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
    def search(self, data):
            temp=self.start
            while temp.next is not None:
                if temp.item is data:
                    return temp
                temp=temp.next
            return None
    def insert_after(self, temp, data):
        if temp is not None:
            n=Node(data, temp.next)
            temp.next = n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp = temp.next
    def delete_first(self):
        if self.start is not None:
            self.start= self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            i = self.start
            j = self.start.next
            while j.next is not None:
                i=i.next
                j=j.next
            i.next= None
    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item is data:
                self.start = None
        else:
            temp = self.start
            if temp.item is data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item is data:
                        temp.next = temp.next.next
                        break
                    temp= temp.next


myList = SLL()
myList.insert_at_start(20)
myList.insert_at_last(34)
myList.insert_at_last(56)
myList.insert_at_last(78)
myList.delete_item(34)
myList.print_list()


       




        
            
            



















