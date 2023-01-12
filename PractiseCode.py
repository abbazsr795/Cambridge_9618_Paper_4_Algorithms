class Person():
    name : str
    age : int
    isMale : bool
    def __init__(self,isMMale,name,age):
        self.name = name
        self.age = age
        self.isMale = isMMale

def readData():
    array = []
    try:
        x = open("/Users/abbazs/Desktop/AS Python /file1.txt", "r+")
        temp = x.readlines()
        for val in range(0,len(temp) -1, 3):
            array.append(Person(name=(temp[val]).strip(),age=int((temp[val + 1]).strip()),isMMale=bool((temp[ val + 2]).strip())))
        return array
    except:
        print("file not found")    
x = readData()
for val in x:
    print(val.name, val.age, val.isMale)