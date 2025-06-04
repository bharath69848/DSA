#Method-1
res = []
def reverse1(arr,index):
    if index == -1: return
    res.append(arr[index])
    reverse1(arr,index-1)
arr = [123,464,54,4964651,464651,23]
reverse1(arr,len(arr)-1)
print(res)

#Method-2
arr = [123,464,54]
def reverse2(arr,start,end):
    if start<end:
        arr[start],arr[end] = arr[end],arr[start]
        reverse2(arr,start+1,end-1)
reverse2(arr,0,len(arr)-1)
print(arr)