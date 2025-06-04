arr = [1,1,1,1,2,2,2,3,4,5,5,2]
last_dup = 1
for i in range(1,len(arr)):
    if arr[i-1]!=arr[i]:
        arr[last_dup] = arr[i]
        last_dup += 1
print("Array -->",arr)