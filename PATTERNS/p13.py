n = int(input("No of Lines: "))
ans = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(ans,end=" ")
        ans+=1
    print()
