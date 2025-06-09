#method-1
'''n = 3
k = 10
arr = [2,3,5,1,9]
res = 0

for i in range(len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum += arr[j]
        if sum==k:
            res = max(res,j-i+1)
print(res)  '''

'''#method2
n = 3
k = 10
arr = [2,3,5,1,9]
res = 0
Sum = 0
dic = {}

for i in range(len(arr)):
    Sum += arr[i]
    if Sum == k:
        res = max(res,i+1)
    rem = Sum-k
    if rem in dic:
        length = i-(dic[rem])
        res = max(res,length)
    if Sum not in dic:
        dic[Sum] = i
print(res)'''

#method3
nums = [10, 5, 2, 7, 1, 9]
res = 0
n = len(nums)
k = 15
s = nums[0]
l,r = 0,0
while r<n:
    while(l<=r and s>k):
        s -= nums[l]
        l += 1
    if s == k:
        res = max(res,r-l+1)
    r+=1
    if r<n:
        s += nums[r]
print(res)