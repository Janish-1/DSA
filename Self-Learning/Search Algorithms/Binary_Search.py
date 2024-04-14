# Iterate from arr[1] to arr[N] over the array. 
# Compare the current element (key) to its predecessor. 
# If the key element is smaller than its predecessor, compare it to the elements before.
# Move the greater elements one position up to make space for the swapped element.


def binarySearch(arr,left,right,x):
    while left<=right:
        mid = left+(right-left) // 2

        # If element is at mid , return mid
        if arr[mid] == x:
            return mid
        
        # If x is greater, ignore left half
        elif arr[mid] < x:
            left = mid + 1

        # If element is less than middle value
        else:
            right = mid - 1
    
    return -1

def binarySearchrecursive(array,left,right,elementtobefound):
    if right >= left:
        mid = left + (right-left) // 2
        if array[mid] == elementtobefound:
            return mid
        elif array[mid] > elementtobefound:
            return binarySearch(array,left,mid-1,elementtobefound)
        else:
            return binarySearch(array,mid+1,right,elementtobefound)
    else:
        return -1
        
arr = [2,3,50,30,40]
arr.sort()
x = 50
result = binarySearch(arr,0,len(arr),x)
print(result)

arr1 = [23,34,65,75,89]
arr1.sort()
x = 65
print(binarySearchrecursive(arr1,0,len(arr1),x))