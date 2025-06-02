#Combine Both the p-7 and p-8
n = int(input("No of Lines: "))
for i in range(n):
    spaces = n-i-1
    stars = (2*i)+1
    for s1 in range(spaces):
        print(" ",end="")
    for star in range(stars):
        print("*",end="")
    for s2 in range(spaces):
        print(" ",end="")
    print()
for i in range(n-1,-1,-1):
    stars = (2*i)+1
    spaces = n-i-1
    for s1 in range(spaces):
        print(" ",end="")
    for star in range(stars):
        print("*",end="")
    for s2 in range(spaces):
        print(" ",end="")
    print()