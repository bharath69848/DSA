def sumofn(N,res=0):
    if N==0: return(res)
    res += N
    return sumofn(N-1,res)
print(sumofn(4))