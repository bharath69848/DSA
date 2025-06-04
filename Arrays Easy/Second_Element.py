#Method-1
arr = [2,5,7,8,9,1]
very_big = 0
big = 0
for i in arr:
    very_big = max(very_big,i)

for i in arr:
    if i>big and i<very_big:
        big = i

print("First Big:",very_big)
print("Second Big:",big)

#Method-2:
arr = [2,5,7,8,1]
veryverybig = 0
bigbig = 0
for i in arr:
    if i>veryverybig:
        bigbig = veryverybig
        veryverybig = i
    elif i>bigbig and i<veryverybig:
        bigbig = i

print("First Big:",veryverybig)
print("Second Big:",bigbig)