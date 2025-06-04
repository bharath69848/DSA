def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

nums = [1,2,3,4,5,6,7]
k = 3
k = k%len(nums)
if k==0: print(nums)
front = len(nums)-k
reverse(nums,0,front-1)
reverse(nums,front,len(nums)-1)
reverse(nums,0,len(nums)-1)
print(nums)