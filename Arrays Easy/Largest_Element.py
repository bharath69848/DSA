arr = [2,5,7,8,9,1,11,22,55464,121649,15133,489654,1543]
very_big = 0
for i in arr:
    if very_big<i:
        very_big = i
print("Largest Element: ",very_big)