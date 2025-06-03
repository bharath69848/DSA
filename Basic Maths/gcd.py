n1 = int(input("N1: "))
n2 = int(input("N2: "))
while n1>0 and n2>0:
    if n1>n2:
        n1 = n1%n2
    else:
        n2 = n2%n1
if n1==0:
    print("GCD: ",n2)
else:
    print("GCD: ",n1)