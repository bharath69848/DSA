n = int(input("No of Lines: "))
for i in range(n,0,-1):
    res = 65
    for j in range(1,i+1):
        print(chr(res),end="")
        res+=1
    print()
