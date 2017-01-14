from Euler import *

n = 1000000
isprime = prime_sieve(n*10)

c = 0

for i in range(1, n+1):
    if not isprime[i]: continue
    sn = list(str(i))
    prime = True
    for r in range(len(sn)):
        sn = sn[1:]+[sn[0]]
        if not isprime[int("".join(sn))]:
            prime = False
    if prime:
        c+=1
verify(c)
