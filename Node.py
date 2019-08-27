from playsound import playsound
sound = False

class Node(object):
    def __init__(self, data):
        self.data = data
        self.smallByte = None
        self.bigByte = None

    def insert(self, data):
        if self.data == data or ' '.join(format(ord(x), 'b') for x in str(self.data)) == ' '.join(format(ord(x), 'b') for x in str(data)):
            return False
        
        elif ' '.join(format(ord(x), 'b') for x in str(data)) < ' '.join(format(ord(x), 'b') for x in str(self.data)):
            if self.smallByte:
                return self.smallByte.insert(data)
            else:
                self.smallByte = Node(data)
                return True

        else:
            if self.bigByte:
                return self.bigByte.insert(data)
            else:
                self.bigByte = Node(data)
                return True

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.smallByte is not None):
            current = current.smallByte

        return current
    
    '''Delete Node '''
    def delete(self, data):
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if ' '.join(format(ord(x), 'b') for x in str(data)) < ' '.join(format(ord(x), 'b') for x in str(self.data))or self.smallByte is not None:
            self.smallByte = self.smallByte.delete(data)
        elif ' '.join(format(ord(x), 'b') for x in str(data)) > ' '.join(format(ord(x), 'b') for x in str(self.data)) or self.bigByte is not None:
            self.bigByte = self.bigByte.delete(data)
        else:
            # deleting node with one child
            if self.smallByte is None:
                temp = self.bigByte
                self = None
                return temp
            elif self.bigByte is None:
                temp = self.smallByte
                self = None
                return temp

            temp = self.minValueNode(self.bigByte)
            self.data = temp.data
            self.bigByte = self.bigByte.delete(temp.data)

        return self

    def find(self, data):
        if(data == self.data):
            if sound :
                playsound('src/click.mp3')
            return True
        elif(' '.join(format(ord(x), 'b') for x in str(data)) < ' '.join(format(ord(x), 'b') for x in str(self.data))):
            if self.smallByte:
                return self.smallByte.find(data)
            else:
                if sound :
                    playsound('src/click4.mp3')
                return False
        else:
            if self.bigByte:
                return self.bigByte.find(data)
            else:
                if sound :
                    playsound('src/click4.mp3')
                return False

    def preorder(self):
        if self:
            print(str(self.data))
            if self.smallByte:
                self.smallByte.preorder()
            if self.bigByte:
                self.bigByte.preorder()

    def inorder(self):
        if self:
            if self.smallByte:
                self.smallByte.inorder()
            print(str(self.data))
            if self.bigByte:
                self.bigByte.inorder()

    def postorder(self):
        if self:
            if self.smallByte:
                self.smallByte.postorder()
            if self.bigByte:
                self.bigByte.postorder()
            print(str(self.data))
