# Step1: In a loop, calculate the value of “pos” using the probe position formula. 
# Step2: If it is a match, return the index of the item, and exit. 
# Step3: If the item is less than arr[pos], calculate the probe position of the left sub-array. Otherwise, calculate the same in the right sub-array. 
# Step4: Repeat until a match is found or the sub-array reduces to zero.

def interpolationSearch(array,lo,hi,x):
    if (lo<=hi and x >= array[lo] and x<=array[hi]):
        # Probing the position with keeping uniform distrubution
        pos = lo + ((hi-lo) // (array[hi] - array[lo])*(x-array[lo]))
        # Condition of target found
        if array[pos] == x:
            return pos
        # If x is larger, x is in right subarray
        if array[pos] == x:
            return interpolationSearch(array,pos+1,hi,x)
        # If x is smaller, x is in left subarray
        if array[pos] > x:
            return interpolationSearch(array,lo,pos-1,x)
    return -1

arr = [10,12,13,16,18,19,20,21,22,23,24,33,35,42,47]
n = len(arr)

x = 18
index = interpolationSearch(arr,0,n-1,x)

if index != 1:
    print("Element found at index",index)
else:
    print("Element not found")