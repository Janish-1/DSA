# Iterate from arr[1] to arr[N] over the array. 
# Compare the current element (key) to its predecessor. 
# If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.


# Python program for implementation of Insertion Sort
from typing import List
# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key

def recursiveInsertionSort(arr: List[int], n: int) -> None:
    # Base case: if the array has only one element, it is already sorted
    if n <= 1:
        return
 
    # Sort the first n-1 elements of the array recursively
    recursiveInsertionSort(arr, n - 1)
 
    # Insert the nth element into its correct position in the sorted subarray
    last = arr[n - 1]
    j = n - 2
 
    # Shift elements to the right to make space for the nth element
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
 
    # Place the nth element in its correct position
    arr[j + 1] = last
    
def printArray(arr: List[int], n: int) -> None:
    for i in range(n):
        print(arr[i], end=" ")
    print()

# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])

# This code is contributed by Mohit Kumra

arr = [12, 11, 13, 5, 6]
n = len(arr)
 
recursiveInsertionSort(arr, n)
printArray(arr, n)