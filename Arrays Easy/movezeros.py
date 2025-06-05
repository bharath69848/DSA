j = 0
arr = [1,0,1,0,5,3]
print(arr)
for i in range(len(arr)):
    if arr[i]!=0:
        arr[i],arr[j] = arr[j],arr[i]
        j +=1 
        print(arr,"change")
    print(arr)
print(arr)