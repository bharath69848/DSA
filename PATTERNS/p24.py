#Combine Both the p-7 and p-8
n = 12
n1,n2 = 0,0
letter = 65

if n%2 == 0:
    n1 += n//2
    n2 += n//2
else:
    n1 += n//2 + 1
    n2 += n//2

for i in range(n1):
    spaces = n1-i-1
    stars = (2*i)+1
    for s1 in range(spaces):
        print(" ",end=" ")
    for star in range(stars):
        if star == 0 or star == stars-1:
            print(chr(letter),end=" ")
        else:
            print(" ",end=" ")
    for s2 in range(spaces):
        print(" ",end=" ")
    letter += 1
    print()
for i in range(n2-1,-1,-1):
    stars = (2*i)+1
    spaces = n1-i-1
    for s1 in range(spaces):
        print(" ",end=" ")
    for star in range(stars):
        if star == 0 or star == stars-1:
            print(chr(letter),end=" ")
        else:
            print(" ",end=" ")
    for s2 in range(spaces):
        print(" ",end=" ")
    letter+=1
    print()