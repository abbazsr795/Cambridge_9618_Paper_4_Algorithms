file2 = open("./My Algorithms/File2.txt", "w")
file2.writelines("abbazs\nyeet\n")
file2.close()
file2 = open("./My Algorithms/File2.txt", "a")
file2.write("gdyedgeyde\n")
file2.close()
file2 = open("./My Algorithms/File2.txt", "r")
print(file2.readlines())
file2.close()


# ("a") appends to the end of the file  -->  file2.writelines("this is a text \n line2 \n line3")
# ("w") overwrites eveything in the file  -->  file2.writelines("this is a text \n line2 \n line3")
# the above code can also be written as -->  file2.writelines(["this is a text\n","line2\n","line3\n"]) basically putting each line in a list element
# ("r") prints an array of strings where each line is an item  -->  print(file2.readlines()) Note that at the end of each element you will get a "\n"

#Note that the key to solve the problem is in the open format. for read only use r and for write only use w