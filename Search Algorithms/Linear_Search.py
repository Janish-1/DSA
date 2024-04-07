# Step 1: First, read the search element (Target element) in the array.
# Step 2: Set an integer i = 0 and repeat steps 3 to 4 till i reaches the end of the array.
# Step 3: Match the key with arr[i].
# Step 4: If the key matches, return the index. Otherwise, increment i by 1.


def search(arr,N,x):
    for i in range(0,N):
        if(arr[i] == x):
            return i
    return -1

arr = [1,2,3,4,5]
x = 5
N = len(arr)

print("Element found at index:",search(arr,x,N))