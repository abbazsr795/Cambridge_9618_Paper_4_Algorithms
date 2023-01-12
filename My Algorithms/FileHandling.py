x = open("/Users/abbazs/Desktop/AS Python /My Algorithms/ReadMe.txt", "a")
x.writelines("")
x.close

x = open("/Users/abbazs/Desktop/AS Python /My Algorithms/ReadMe.txt", "r")
print(x.readlines())
x.close()

x = open("/Users/abbazs/Desktop/AS Python /My Algorithms/ReadMe.txt", "a")
x.write("hello there \n")
x.close