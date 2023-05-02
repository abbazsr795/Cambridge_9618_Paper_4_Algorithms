import pickle 
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
x = Person("abbazs", 18)
y = Person("Azeem", 17)
z = Person("Gopal", 12)

file1 = open("./My Algorithms/File1.dat", "wb") #Write data
pickle.dump(y,file1)
file1.close()
file1 = open("./My Algorithms/File1.dat", "rb") #Read data
yeet = pickle.load(file1)
print(yeet.name)
file1.close()
