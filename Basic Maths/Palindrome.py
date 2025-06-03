#Method-1
n = int(input("Number: "))
check = n
res = 0
while n:
    digit = n%10
    res = res*10 + digit
    n = n//10
if check == res:
    print("True")
else:
    print("False")

#Method-2
n = int(input("Number: "))
check = str(n)
if n == int(check[::-1]):
    print("True")
else:
    print("False")

#Method-3
n = input("Number: ")
i,j = 0,len(n)-1
while i<j:
    if n[i]!=n[j]:
        print("False")
        exit()
    i+=1
    j-=1
print("True")