#Method-1
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
#Method-2
n = int(input("No of Lines: "))
col = (2*n)-1
for i in range(n):
    stars = (2*i)+1
    spaces = (col-stars)//2
    for s1 in range(spaces):
        print(" ",end="")
    for star in range(stars):
        print("*",end="")
    for s2 in range(spaces):
        print(" ",end="")
    print()