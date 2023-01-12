#This section is complete
array = [3,1,2,5,2,3,46,7,44,654,6544]
x = len(array)
y = 0
sort = True
while(y < len(array)) and sort:
    sort = False
    for val2 in range(x - 1):
        if array[val2] > array[val2 + 1]:
            temp = array[val2]
            array[val2] = array[val2 + 1]
            array[val2 + 1] = temp
            sort = True
    y = y + 1
    x = x - 1
print(array)

# # Another method
# x = len(array) - 1
# found = False
# for val in range(len(array) - 1):
#     for val2 in range(x):
#         if array[val2] > array[val2 + 1]:
#             temp = array[val2]
#             array[val2] = array[val2 + 1]
#             array[val2 + 1] = temp
#             found = True
#     if found:
#         break
# print(array)