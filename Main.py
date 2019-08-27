#!/bin/python
from Tree import Tree
from random import randrange
import random
import string
import time
from progress.bar import ShadyBar

tree = Tree()
dataSet1 = []
dataSet2 = []
dataset1Size = 10000000
searchKeySize = 10

##Genarate random Strings
letters = 'al34nMT0V&#@fr'
def randString(letters):
    return ''.join((random.choice(letters) for i in range(randrange(10))))

'''
##Genarate random dataset
print('Genarating dataset...')
with open('dataSet1.txt', 'w') as filehandle:
    for counter in range(0,dataset1Size):
        randomstring = randString(letters)
        filehandle.write('%s\n' % randomstring)
        dataSet1.append(randomstring)
        tree.insert(randomstring)
     
##Genarate random search keys
print('Genarating search keys...')
with open('searchKeys.txt', 'w') as filehandle:
    for counter in range(0,searchKeySize):
        randkey = randString(letters)
        dataSet2.append(randkey)
        filehandle.write('%s\n' % randkey)
        
##Read datasets
print('Reading dataset...')
with open('dataSet1.txt', 'r') as filehandle:
    for line in filehandle:
        currentValue = line[:-1]
        dataSet1.append(currentValue)
        tree.insert(currentValue)
        
print('Reading search keys...')     
with open('searchKeys.txt', 'r') as filehandle:
    for line in filehandle:
        currentValue = line[:-1]
        dataSet2.append(currentValue)
'''

##Genarate random dataset  
with ShadyBar('Genarating dataset...', max=100) as bar:
    for counter1 in range(0,dataset1Size):
        randomstring = randString(letters)
        dataSet1.append(randomstring)
        tree.insert(randomstring)
        if counter1/dataset1Size*100 in range(0,100) :
            bar.next()


##Genarate random search keys
with ShadyBar('Genarating search keys...', max=100) as bar:
    for counter2 in range(0,searchKeySize):
        dataSet2.append(randString(letters))
        if counter2/searchKeySize*100 in range(0,100) :
            bar.next()
            

print('\nDataset includes ',len(dataSet1),' data')
print(len(dataSet2),' search keys')
print('======================================================================')

##Search option 1
start1 = time.time()
for data in dataSet2:
    print('Find ',data,' \t:',tree.find(data))
end1 = time.time()
print('===============Option 1 Execution time : %s seconds ==================\n' %round(end1-start1,2))

##search option 2
start2 = time.time()
for searchIndex in dataSet2:
    for index in dataSet1:
        if index == searchIndex:
            print('Find ',searchIndex,' \t: True')
            break
        index = None
    print('Find ',searchIndex,' \t: False')
searchIndex = None

end2 = time.time()
print('===============Option 2 Execution time : %s seconds ==================' %round(end2-start2,2))
print('======================================================================')
print('Option 1 Execution efficiency %s/100' %round(((end2-start2)-(end1-start1)/(end2-start2))*100,2))
#print(tree.postorder())



