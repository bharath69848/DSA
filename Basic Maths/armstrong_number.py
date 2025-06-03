import math
n = int(input("Number: "))
length = int(math.log(n,10)+1)
check = n
armstrong = 0
while n:
    digit = n%10
    armstrong += digit**length
    n = n//10
print(True) if check==armstrong else print(False)