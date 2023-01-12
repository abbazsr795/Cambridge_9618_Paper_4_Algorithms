#This section is complete
array = [1,2,23,44,75,432,5974]
lb = 0
ub = len(array) - 1
found = False
search_value = 4
while not(ub<lb) and not(found):
    mid = int((lb + ub)/2)
    if array[mid] == search_value:
        print("It's there!")
        found = True
    elif array[mid] < search_value:
        lb = mid + 1
    else:
        ub = mid - 1
if not(found):
    print("It's not there")