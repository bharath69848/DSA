arr = [4, 7, 1, 0]
maxx = arr[-1]
res = []
for i in range(len(arr)-1,-1,-1):
    if not res or res[-1]!=maxx:
        res.append(maxx)
    maxx = max(arr[i],maxx)
print(res[::-1])