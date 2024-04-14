# The idea is to start with subarray size 1, compare its last element with x, then try size 2, then 4 and so on until last element of a subarray is not greater. 
# Once we find an index i (after repeated doubling of i), we know that the element must be present between i/2 and i (Why i/2? because we could not find a greater value in previous iteration)


def binarySearch(array,left,right,x):
    if right >= left:
        mid = left + (right-left) // 2
        # If element is present at the middle itself
        if array[mid] == x:
            return mid
        # If the element is smaller than mid,then it can only be present in the left subarray
        if array[mid] > x:
            return binarySearch(array,left,mid-1,x)
        # If element can only be present in the right 
        return binarySearch(array,mid+1,right,x)
    
    return -1

def exponentialSearch(array,n,x):
    # If x is present at first location itself
    if array[0] == x:
        return 0
    # Find range for binary search j by repeted doubling
    i = 1
    while i < n and array[i] <= x:
        i = i * 2

    return binarySearch(array,i//2,min(i,n-1),x)

arr = [2,3,4,10,40]
n = len(arr)
x = 10
result = exponentialSearch(arr,n,x)
if result == -1:
    print("Element not found in the array")
else:
    print("Element is present at index %d"%(result))
    