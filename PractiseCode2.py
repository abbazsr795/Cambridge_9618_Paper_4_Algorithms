#a)

#QueueArray as Array of 10 Strings
#HeadPointer as Integer
#TailPointer as Integer
#NoOfItems as Integer
QueueArray = [None for val in range(10)]
HeadPointer = 0
TailPointer = 0
NoOfItems = 0

#b)

def Enqueue(ItemAdd):
    global QueueArray, HeadPointer, TailPointer, NoOfItems
    if NoOfItems == 10:
        return False
    QueueArray[TailPointer] = ItemAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1
    NoOfItems = NoOfItems + 1
    return True

#c)

def Dequeue():
    global QueueArray, HeadPointer, TailPointer, NoOfItems
    if NoOfItems == 0:
        return False
    else:
        temp = HeadPointer
        if HeadPointer == 9:
            HeadPointer = 0
        else:
            HeadPointer = HeadPointer + 1
        NoOfItems = NoOfItems - 1
        x =  QueueArray[temp]
        QueueArray[temp] = None
        return x

#d)i)

for val in range(11):
    x = input("your input : ")
    if Enqueue(x):
        print("Item added")
    else:
        print("Failded to add item")
for val in range(2):
    x = Dequeue()
    if x == False:
        print("No more items")
    else:
        print(f"{x} removed")
    
