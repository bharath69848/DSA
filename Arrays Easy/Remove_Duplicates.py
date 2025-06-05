arr = [1,1,1,1,2,2,2,3,4,5,5,2]
j = 1
for i in range(1,len(arr)):
    if arr[i-1] != arr[i]:
        arr[j] = arr[i]
        j+=1
print(arr)