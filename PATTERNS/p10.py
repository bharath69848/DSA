n = 5
rows = (2*n)-1
for i in range(1,rows+1):
    if i>=n:
        for j in range((2*n)-i):
            print('*',end="")
        print()
    else:
        for k in range(1,i+1):
            print("*",end="")
        print()