n = int(input("Length Of the Square: "))
if n==1:
    print("*")
    exit()
print("*"*n)
for i in range(n-2):
    print('*',end="")
    for space in range(n-2):
        print(" ",end="")
    print("*",end="")
    print()
print("*"*n)
