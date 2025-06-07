n=int(input("Square Length: "))
for i in range(2*n-1):
    for j in range(2*n-1):
        top,down,left,right = i,2*n-2-i,j,2*n-2-j
        print(n-min(top,down,left,right),end=" ")
    print()
