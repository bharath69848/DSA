#Method-1
n = int(input("Number: "))
divisors = []
for i in range(1,n+1):
    if n%i==0:
        divisors.append(i)
print("Divisor: ",end="")
for i in divisors:
    print(i,end=" ")
print()
#Method-2
n = int(input("Number: "))
divi = []
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        divi.append(i)
        if n/i != i:
            divi.append(n//i)
print("Divisor: ",end="")
for i in divi:
    print(i,end=" ")