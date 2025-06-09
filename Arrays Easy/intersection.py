#method1 
num1 = [1,2,2,3,3,4,5,6]
num2 = [2,3,3,5,6,6,7]
visited = [0]*len(num2)
res = []

for i in range(len(num1)):
    for j in range(len(num2)):
        if num1[i] ==  num2[j] and visited[j] == 0:
            res.append(num1[i])
            visited[j] = 1
            break
        elif num2[j] > num1[i]:
            break
print(res)

#method2 two pointers
res2 = []
i,j = 0,0
while i<len(num1):
    if num1[i] > num2[j]:
        j += 1
    elif num1[i] < num2[j]:
        i+=1
    else:
        res2.append(num1[i])
        i += 1
        j += 1
print(res2)
