n = 5
start = 64+n
for i in range(1,n+1):
    ss = start
    for j in range(1,i+1):
        print(chr(ss),end="")
        ss += 1
    start-=1
    print()
