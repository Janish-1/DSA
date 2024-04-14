# First, we compare the key with the element at mid1. If found equal, we return mid1.
# If not, then we compare the key with the element at mid2. If found equal, we return mid2.
# If not, then we check whether the key is less than the element at mid1. If yes, then recur to the first part.
# If not, then we check whether the key is greater than the element at mid2. If yes, then recur to the third part.
# If not, then we recur to the second (middle) part.


import math as mt

def ternarySearch(left,right,key,array):
    while right >= left:
        mid1=left+(right-left)//3
        mid2=right-(right-left)//3
        if key==array[mid1]:
            return mid1
        if key==array[mid2]:
            return mid2
        if key < array[mid1]:
            right=mid1-1 # Key lies between left and mid1
        elif key > array[mid2]:
            left=mid2+1 # Key lies between right and mid2
        else:
            left = mid1 + 1
            right = mid2 + 1

    return -1   

def ternarySearchrecursive(left,right,key,array):
    if right >= left:
        # Find the mid1 and mid2
        mid1 = left + (right-left) // 3
        mid2 = right - (right-left) // 3
        # Check if key is present at any mid 
        if (array[mid1] == key):
            return mid1
        if (array[mid2] == key):
            return mid2
        # If key is not present at mid
        if (key<array[mid1]):
            # Key lies between left and middle1
            return ternarySearchrecursive(left,mid1-1,key,array)
        elif (key<array[mid2]):
            # Key lies between middle2 and right
            return ternarySearchrecursive(mid2+1,right,key,array)
        else:
            # Key lies between middle1 and middle2
            return ternarySearchrecursive(mid1+1,mid2-1,key,array)
        
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
l,r,k = 0,len(arr),8
print(ternarySearchrecursive(l,r,k,arr))
print(ternarySearch(l,r,k,arr))