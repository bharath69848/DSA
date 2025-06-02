n = 5
rows = (2*n)-1
for i in range(1,rows+1):
    if i>n:
        stars = (2*n)-i
        spaces = (2*n) - (stars*2)
        for l in range(stars):
            print("*",end="")
        for j in range(spaces):
            print(" ",end="")
        for k in range(stars):
            print("*",end="")
        print()
    else:
        stars = i
        spaces = (2*n) - (stars*2)
        for l in range(stars):
            print("*",end="")
        for j in range(spaces):
            print(" ",end="")
        for k in range(stars):
            print("*",end="")
        print()