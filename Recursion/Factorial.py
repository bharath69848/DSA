#Method-1
def fact1(n,res=1):
    if n==0:
        return res
    res *= n
    return fact1(n-1,res)
print(fact1(10))

#Method-2
def fact2(n):
    if n==1:
        return 1
    return n*fact2(n-1)
print(fact2(10))