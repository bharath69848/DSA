n = 5
s1 = 0
s2 = 2*(n-1)
for i in range(n,0,-1):
    stars = i
    for star in range(stars):
        print("*",end="")
    for space in range(s1):
        print(" ",end="")
    for star in range(stars):
        print("*",end="")
    s1 += 2
    print()

for i in range(1,n+1):
    stars = i
    for star in range(stars):
        print("*",end="")
    for space in range(s2):
        print(" ",end="")
    for star in range(stars):
        print("*",end="")
    s2 -= 2
    print()