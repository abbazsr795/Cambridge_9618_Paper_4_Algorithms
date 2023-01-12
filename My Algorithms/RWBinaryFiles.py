import pickle 
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
x = Person("abbazs", 18)
y = Person("Azeem", 17)
z = Person("Gopal", 12)

file1 = open("/Users/abbazs/Desktop/AS Python /My Algorithms/File1.dat", "r+b")
# write --->  pickle.dump (x,file1)
# read ---> yeet = pickle.load(file1)
# print ---> print(yeet.name)
file1.close()