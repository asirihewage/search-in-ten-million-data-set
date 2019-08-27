# Search in ten million data set
This python script will demonstrate how to use Binary Tree to perform searching in ten million dataset. Traditional Binary tree with Byte sence :D

# run in console

```Python
  >> python3 Main.py
```

# implementation

```Python
#!/bin/python
from Tree import Tree
from random import randrange
import random
import string
import time
from progress.bar import ShadyBar

dataSet1 = []
dataSet2 = []
dataset1Size = 10000000
searchKeySize = 10

##Genarate random Strings
letters = 'al34nMT0V&#@fr'
def randString(letters):
    return ''.join((random.choice(letters) for i in range(randrange(10))))
    
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
```

## Search Option 1 using the tree

```Python
##Search option 1
start1 = time.time()
for data in dataSet2:
    print('Find ',data,' \t:',tree.find(data))
end1 = time.time()
```

## Search option 2 using traditional array
```Python
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
```

![Ten Million Data set](https://github.com/asirihewage/search-in-ten-million-data-set/blob/master/screenshots/10%20million%20data.png)
![IDLE](https://github.com/asirihewage/search-in-ten-million-data-set/blob/master/screenshots/pythonIDLE.png)
![CMD](https://github.com/asirihewage/search-in-ten-million-data-set/blob/master/screenshots/CMD.png)
