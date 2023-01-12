#This section is complete
array = [3,1,2,5,2,3,46,7,44,654,200000]
for val in range(1,len(array)):
    x = val - 1
    y = array[val]
    if y < array[x]:
        while (y < array[x]) and (x >= 0):
            temp = array[x + 1]
            array[x + 1] = array[x]
            array[x] = temp
            x = x - 1 
print(array)