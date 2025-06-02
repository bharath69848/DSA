n = int(input("No of Lines: "))
col = 2*n
for i in range(n):
    nums = i+1
    spaces = col-(nums*2)
    for num in range(1,nums+1):
        print(num,end="")
    for space in range(spaces):
        print(" ",end="")
    for num in range(nums,0,-1):
        print(num,end="")
    print()