class Node():
    def __init__(self, value, left = None, right =None):
        self.left = left
        self.right = right
        self.value = value
    def addItem(self,x):
        if x > self.value:
            if self.right == None:
                self.right = x
            else:
                self.right.addItem(x)
        else:
            if self.left == None:
                self.left = x
            else:
                self.left.addItem(x)
    def searchItem(self, x):
        while (self.value != x):
            if x < self.value:
                if self.left != None:
                    self.left.search(x)
                    return
                else:
                    print("not available")
                    return
            if x > self.value:
                if self.right != None:
                    self.right.search(x)
                    return
                else:
                    print("not available")
                    return
        print(self.value)