class Node:
    def __init__(self,left=None, item=None, right=None):
        self.left = left
        self.item = item
        self.right = right
class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        self.root = self.rinsert(self.root,data)
    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item :
            root.left = self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root
    def search(self,data):
        return self.rsearch(self.root, data)
    def rsearch(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right, data)


        

