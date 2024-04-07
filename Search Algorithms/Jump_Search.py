# Jump Search is an algorithm for finding a specific value in a sorted array by jumping through certain steps in the array.
# The steps are determined by the sqrt of the length of the array. 
# Here is a step-by-step algorithm for the jump search:
# Determine the step size m by taking the sqrt of the length of the array n.
# Start at the first element of the array and jump m steps until the value at that position is greater than the target value.
# Once a value greater than the target is found, perform a linear search starting from the previous step until the target is found or it is clear that the target is not in the array.
# If the target is found, return its index. If not, return -1 to indicate that the target was not found in the array. 



import math

def jumpSearch(array,x,n):
    # Block size to be jumped
    step = math.sqrt(n)
    # Finding the block where element is present
    prev = 0
    while array[int(min(step,n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    # Doing a linear search for x in block begining with prev
    while array[int(prev)] < x:
        prev += 1
        # If we reached next block or end of array,element is not present
        if prev == min(step,n):
            return -1
    # If element is found
    if array[int(prev)] == x:
        return prev
    
arr = [0,1,2,3,4,6,8,13,21,34,55,89,144,169,233,377,610]
x = 55
n = len(arr)

index = jumpSearch(arr,x,n)
print("Number",x,"is at index","%.0f"%index)