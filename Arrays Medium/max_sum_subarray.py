#m1
'''
for i in range(len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum += arr[j]
        m_sum = max(m_sum,sum)
print(m_sum)
'''
#m2
arr = [-2,1,-3,4,-1,2,1,-5,4] 
sum = float('-inf')
max_sum = float('-inf')
l,r = 0,0
for i in range(len(arr)):
    sum = max(sum+arr[i],arr[i])
    if sum+arr[i]>arr[i]:
        l=i
        sum = sum+arr[i]
    else:
        sum = arr[i]
    if max_sum<sum:
        max_sum = sum
        r = i
print(r-l)

