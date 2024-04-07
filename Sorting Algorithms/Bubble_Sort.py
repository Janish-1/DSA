# Run a nested for loop to traverse the input array using two variables i and j, such that 0 ≤ i < n-1 and 0 ≤ j < n-i-1
# If arr[j] is greater than arr[j+1] then swap these adjacent elements, else move on
# Print the sorted array

def bubbleSort(array):
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0,n-i-1):
            # Traverse array from 0 to n-i-1
            if array[j] > array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]

arr = [5,1,4,2,8]
bubbleSort(arr)
print(arr)