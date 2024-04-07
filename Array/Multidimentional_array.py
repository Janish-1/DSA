# 2D Array
arr = [[1,2,3],[4,5,6],[7,8,9]]
# 3D Array
arr1 = [[[1,2,3],[4,5,6]],[[7,8,9]]]


for i in range(len(arr)):
    for j in range(3):
        print("2D Array: ",arr[i][j],end=" ")

for i in range(2):
    for j in range(2):
        for k in range(3):
            print("3D Array: ",arr[i][j][k],end=" ")