#Method-1
n = int(input("Enter a Number: "))
count = 0
while n:
    count += 1
    n = n//10
print("Digits: ",count)

#Method-2
import math
n = int(input("Enter a Number: "))
digits = math.log(n,10) + 1
print("Digits: ",int(digits))