n = [1,5,8,6,2,4]
search = int(input())
for i in range(len(n)):
    if n[i] == search:
        print("Found:",i)
        exit()
print("Not found")