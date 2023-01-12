def BinarySearch(top,bottom,array, item):
    mid = int((top + bottom)/ 2)
    if (array[mid] == item):
        print(mid)
    elif (top < bottom):
        print("item not found")
    else:
        if array[mid] > item:
            top = mid - 1
        if array[mid] < item:
            bottom = mid + 1
        BinarySearch(top,bottom,array,item)

BinarySearch(5,0,[9,32,64,3,88,3], 64)