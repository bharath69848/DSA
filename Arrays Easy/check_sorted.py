arr = [125,456,789]
for i in range(1,len(arr)):
    if arr[i-1]>arr[i]:
        print(arr,"-->","Not Sorted")
        exit()
print(arr,"-->","Sorted")