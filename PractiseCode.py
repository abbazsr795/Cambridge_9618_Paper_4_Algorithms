#In this test you will create functions for each given algorithm

array1 = [7,2,4,99,29,63,543]
array2 = [99,122,881,999,1002,2009]

#Linear search

def LinearSearch(search):
    global array1
    for val in range(len(array1)):
        if array1[val] == search:
            print(f"The value is on {val}")
            break

#Binaryy search (with recursion included)

def BinarySearch(search):
    global array2
    ub = len(array2) - 1
    lb = 0
    found = False
    while ub >= lb:
        mid = int((ub + lb)/2)
        if array2[mid] == search:
            print("The value exists")
            found = True
            break
        elif array2[mid] < search:
            lb = mid + 1
        else:
            ub = mid - 1 
    if not(found):
        print("doesn't exist")

def BinarySearchWithReccusion(array, lb, ub, search):
    if ub >= lb:
        mid = int((lb + ub)/2)
        if array[mid] == search:
            return "Found it"
        elif array[mid] < search:
            return BinarySearchWithReccusion(array, mid + 1, ub, search)
        else:
            return BinarySearchWithReccusion(array, lb, mid - 1, search)
    else:
        return "value not found"

#Insertion sort

def InsertionSort():
    global array1
    for val in range(1, len(array1)):
        x = val - 1
        y = array1[val]
        while (y < array1[x]) and (x >= 0):
            temp = array1[x + 1]
            array1[x + 1] = array1[x]
            array1[x] = temp
            x = x - 1
    print(array1)

#Bubble sort

def BubbleSort():
    global array1
    x = 0
    y = len(array1)
    sort = True
    while (x < len(array1)) and sort:
        sort = False
        for val in range(y - 1):
            if array1[val] > array1[val + 1]:
                temp = array1[val]
                array1[val] = array1[val + 1]
                array1[val + 1] = temp
                sort = True
        x = x + 1
        y= y - 1
    print(array1)

#Stacks 
array3 = [3,7,1,99,3, 0,55]
basePointer = 0
topPointer = 4
stackFull= len(array3)
stackLength = 5
def Pop():
    global array3, topPointer, basePointer, stackLength, stackFull
    if stackLength > 0:
        topPointer = topPointer -1 
        stackLength = stackLength - 1
    else:
        print("Stack is empty")

def Push(value):
    global array3, topPointer, basePointer, stackLength, stackFull
    if stackLength < stackFull:
        topPointer = topPointer + 1
        stackLength = stackLength + 1
        array3[topPointer] = value
    else:
        print("Stack is full")

#Queues
array3 = [3,7,1,99,3, 0,55]
frontPointer = 0
rearPointer = 4
queueFull= len(array3)
queueLength = 5

def enQueue(value):
    global array3, rearPointer, frontPointer, queueLength, queueFull
    if (rearPointer < queueFull - 1):
        rearPointer = rearPointer + 1
        queueLength = queueLength + 1
        array3[rearPointer] = value
    else:
        print("Queueu full")

def deQueue():
    global array3, rearPointer, frontPointer, queueLength, queueFull
    if (queueLength != 0 ):
        frontPointer = frontPointer - 1
        queueLength = queueLength - 1
    else:
        print("Queue is empty")

def enQueueCircle(value):
    global array3, rearPointer, frontPointer, queueLength, queueFull
    if queueLength < queueFull:
        if rearPointer == (queueFull - 1):
            rearPointer = 0
        else:
            rearPointer = rearPointer + 1
        array3[rearPointer] = value
        queueLength = queueLength + 1
    else:
        print("Queue is full")
    print(array3)

def deQueueCircle():
    global array3, rearPointer, frontPointer, queueLength, queueFull
    if queueLength == 0:
        print("Queue is empty")
    else:
        if frontPointer == (queueFull -1):
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1
        queueLength = queueLength - 1
    print(array3)

#Linked list

linkedList =      [3, 2,9,4,19,None,None,None]
linkedListIndex = [-1,0,1,2,3, 6,   7,   8]
startPointer = 4
heapPointer = 5

def SearchLinkedList(value):
    global linkedList, linkedListIndex, heapPointer, startPointer
    x = startPointer
    found = False
    while (x != -1) and not(found):
        if linkedList[x] == value:
            found = True
            break
        else:
            x = linkedListIndex[x]
    if found:
        print(f"Value lies in position {x}")
    else:
        print("value doesb't exist")

def AddLinkedList(value):
    global linkedList, linkedListIndex, heapPointer, startPointer
    if heapPointer == -1:
        print("List is full")
    else:
        temp = startPointer
        startPointer = heapPointer
        linkedList[startPointer] = value
        heapPointer = linkedListIndex[heapPointer]
        linkedListIndex[startPointer] = temp
    for val in range(len(linkedList)):
        print(linkedListIndex[val], linkedList[val])
    
def DelLinkedList(value):
    global linkedList, linkedListIndex, heapPointer, startPointer
    x = startPointer
    found = False
    while (x != -1) and not(found):
        if linkedList[x] == value:
            found = True
            break
        else:
            y = x
            x = linkedListIndex[x]
    if found:
        linkedListIndex[y] = linkedListIndex[x]
        linkedListIndex[x] = heapPointer
        heapPointer = x
    else:
        print("value doesb't exist")
    for val in range(len(linkedList)):
        print(linkedListIndex[val], linkedList[val])

#Text file handling

def readFile():
    textFile = open("/Users/abbazs/School/AS Python/My Algorithms/File2.txt", "r")
    lines = textFile.readlines()
    for val in range(len(lines)):
        lines[val] = lines[val].rstrip('\n')
    print(lines)

def writeFile(value1,value2,value3):
    textFile = open("/Users/abbazs/School/AS Python/My Algorithms/File2.txt", "w")
    textFile.writelines([value1 + '\n',value2 + '\n',value3 + '\n'])

def appendFile(value):
    textFile = open("/Users/abbazs/School/AS Python/My Algorithms/File2.txt", "a")
    textFile.write('\n' + value)

#Binary file handling

import pickle 

def writeFileB(object):
    textFile = open("/Users/abbazs/School/AS Python/My Algorithms/File2.txt", "wb")
    pickle.dump(object, textFile)

writeFileB([1,2,6,5])

def readFileB():
    textFile = open("/Users/abbazs/School/AS Python/My Algorithms/File2.txt", "rb")
    x = pickle.load(textFile)
    print(x)


#Binary trees with OOP

class Node():
    def __init__(self,value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def Search(self,value):
        if self.value != value:
            if (value > self.value) and (self.right != None):
                return self.right.Search(value)
            elif (value < self.value) and (self.left != None):
                return self.left.Search(value)
            if (value > self.value) and (self.right == None):
                return -1
            elif (value < self.value) and (self.left != None):
                return -1
        else:
            return value
    def Add(self, value):
        if self.value == None:
            self.value = value
        else:
            if (value > self.value) and (self.right == None):
                self.right = Node(value=value)
            elif (value > self.value) and (self.right != None):
                self.right.Add(value)
            elif (value < self.value) and (self.left == None):
                self.left = Node(value=value)
            else:
                self.left.Add(value)

#Binary files

import pickle

file = open("/Users/abbazs/School/AS Python/My Algorithms/File1.dat", "wb")
file.seek(1)
pickle.dump(Node(value = "Abbazs"), file)
file.close()
file = open("/Users/abbazs/School/AS Python/My Algorithms/File1.dat", "wb")
file.seek(2)
pickle.dump(Node(value = "Azeem"), file)
file.close()
file = open("/Users/abbazs/School/AS Python/My Algorithms/File1.dat", "wb")
file.seek(3)
pickle.dump(Node(value = "Shimar"), file)
file.close()
file = open("/Users/abbazs/School/AS Python/My Algorithms/File1.dat", "rb")
file.seek(3)
x = pickle.load(file)
print(x.value)