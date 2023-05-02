class Node():
    def __init__(self,value= -1 ,left= -1 ,right= -1):
        self.value = value
        self.left = left
        self.right = right
    def Add(self, x):
        if self.value > x:
            if self.left == -1:
                self.left = Node(x)
            else:
                self.left.Add(x)
        else:
            if self.right == -1:
                self.right = Node(x)
            else:
                self.right.Add(x)
    def Search(self,x):
        if self.value == x:
            print("Found it")
        elif (self.value > x) and self.left != -1:
            self.left.Search(x)
        elif (self.value < x) and self.right != -1:
            self.right.Search(x)
        else:
            print("Its not there")