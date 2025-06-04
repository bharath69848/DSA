n = 3
for i in range(n,0,-1):
    spaces = n - i
    res = n-i+1
    sub = n
    for j in range(spaces):
        print(" ",end="")
    for stars in range(i):
        print(res,end=" ")
        res += sub
        sub -= 1
    print()