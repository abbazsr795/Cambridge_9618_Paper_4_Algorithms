class node:
    def __init__(self,value,pointer):
        self.value = value
        self.pointer = pointer

array = [node(55,3),node(23,2),node(11,-1),node(98,1),node(None,-1,-1),node(None,-1,-1)]
startPointer = 0
heapPointer = 4

def searchLinkedList(list,value):
    global startPointer
    global heapPointer
    itemPointer = startPointer
    while (itemPointer != -1) and (list[itemPointer].value != value):
        itemPointer = list[itemPointer].pointer
    if itemPointer == -1:
        print("item not found")
    else:
        print(itemPointer)

