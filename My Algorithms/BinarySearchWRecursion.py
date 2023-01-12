def binarySearch(array,lower,upper, searchValue):
    if lower <= upper:
        mid = int((lower + upper)/2)
        if array[0][mid] == searchValue:
            return mid
        if array[0][mid] > searchValue:
            return binarySearch(array,lower,mid - 1,searchValue)
        if array[0][mid] < searchValue:
            return binarySearch(array,mid + 1, upper,searchValue)
    return -1 