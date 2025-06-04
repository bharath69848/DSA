def printing(n,count=1):
    if count==n+1: return
    print(count)
    printing(n,count+1)
printing(5)