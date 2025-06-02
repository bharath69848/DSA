n = 4
for i in range(1,n+1):
    spaces = n-i
    letter = 65
    for j in range(spaces):
        print(" ",end="")
    for l in range(1,i+1):
        print(chr(letter),end="")
        letter+=1
    letter-=1
    for ll in range(1,i):
        letter-=1
        print(chr(letter),end="")
    for j in range(spaces):
        print(" ",end="")
    print()
