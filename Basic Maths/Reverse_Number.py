#Method-1
n = int(input("Number: "))
res = 0

while n:
    digit = n%10
    res = res*10 + digit
    n = n//10

print(res)

#Method-2
n = int(input("Number: "))
res = str(n)
print(int(res[::-1]))