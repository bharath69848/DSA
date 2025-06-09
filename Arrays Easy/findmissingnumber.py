#method1
nums = [1,2,4,5]
n = len(nums)
xor1 = 0
xor2 = 0
for i in range(n-1):
    xor2 = xor2^nums[i]
    xor1 = xor1^(i+1)
xor1 = xor1^n
print(xor1^xor2)