def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    prime = [True for i in range(n + 1)]
    prime[0] = False
    prime[1] = False

    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for i in range(len(prime)):
        if prime[i]:
            print(i,end = " ")
            
sieve_of_eratosthenes(100)