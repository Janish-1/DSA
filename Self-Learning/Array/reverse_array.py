arr = [1,2,3,4,5,6,7,8,9]
rev_arr = []
print(arr[::-1])
for i in range(-1,(-1*len(arr)-1),-1):
    rev_arr.append(arr[i])
print(rev_arr)