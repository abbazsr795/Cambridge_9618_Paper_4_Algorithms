#This section is complete
array = [1,2,23,44,75,432,5974]
ub = len(array) - 1
lb = 0
search_item = 5974
for val in range(lb,ub + 1):
    if array[val] == search_item:
        print(val)
        break