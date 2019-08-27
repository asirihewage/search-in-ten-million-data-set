from Node import Node

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Pre order: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('In order: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Post order: ')
            self.root.postorder()

    
