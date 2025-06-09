arr1 = [1] * 100000
arr2 = [2] * 100000
res = []

i,j = 0,0
while i<len(arr1) and j<len(arr2):
    if arr1[i] < arr2[j]:
        if i>0 and arr1[i-1] == arr1[i]:
            i += 1
        else:
            res.append(arr1[i])
            i+=1
    elif arr1[i] > arr2[j]:
        if j>0 and arr2[j-1] == arr2[j]:
            j+=1
        else:
            res.append(arr2[j])
            j+=1
    else:
        if i>0 and arr1[i-1] == arr1[i]:
            i += 1
            j += 1
        elif j>0 and arr2[j-1] == arr2[j]:
            i += 1
            j += 1
        else:
            res.append(arr1[i])
            i+=1
            j+=1

while i < len(arr1):
    if i == 0 or arr1[i] != arr1[i - 1]:
        res.append(arr1[i])
    i += 1

# Handle remaining part of arr2
while j < len(arr2):
    if j == 0 or arr2[j] != arr2[j - 1]:
        res.append(arr2[j])
    j += 1
print(res)