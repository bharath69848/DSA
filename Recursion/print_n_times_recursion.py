def printing(msg,n,count=0):
    if count==n: 
        return
    print(msg)
    printing(msg,n,count+1)

printing("Hi",10)