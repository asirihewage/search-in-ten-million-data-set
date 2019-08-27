#!/bin/python
#from  Tree import Tree

#tree data structure
#baseTree = Tree()

#arrays
NumberDataStore = []
StringDataStore = []
ObjectDataStore = []
root = None

def saveInDataStore(value):
    if type(value) == type(1) or type(value) == type(1.2):
        NumberDataStore.append(value)
        print(value,' saved in number data store')
    elif type(value) == type('str'):
        StringDataStore.append(value)
        print(value,' saved in string data store')
    else:
        ObjectDataStore.append(value)
        print(value,' saved in object data store')
        
    
class Data(object):
    def __init__(self):
        root = Tree()

    ##get numbers
    def getNumberDataStore(self):
        return NumberDataStore
    
    ##get strings
    def getStringDataStore(self):
        return StringDataStore
    
    ##get objects
    def getObjectDataStore(self):
        return ObjectDataStore

    ##save element
    def add(self, value):
        saveInDataStore(value)

            
    def getAll(self):
        return root

    def search(self,index):
        return root.child[0].data[0]

    def insert(self, data):
        root.createChildren(3)
        root.setChildrenValues([5,6,7]) 
        root.child[0].createChildren(2)
        root.child[0].setChildrenValues([1,2])
        return true


        

    
