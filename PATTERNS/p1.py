#Method-1
n = int(input("No of Lines: "))
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

#Method-2
n = int(input("No of Lines: "))
for i in range(n):
    print("*"*n)
