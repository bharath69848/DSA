#Method-1
def sumofn(N,res=0):
    if N==0: return(res)
    res += N
    return sumofn(N-1,res)
print(sumofn(0))

#Method-2
def sumofn2(n):
    if n==0:
        return 0
    return n+sumofn2(n-1)
print(sumofn2(4))