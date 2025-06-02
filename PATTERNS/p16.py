n = int(input())
letter = 65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(letter),end="")
    print()
    letter+=1
