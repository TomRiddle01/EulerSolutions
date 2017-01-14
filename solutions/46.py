from Euler import *

# i = a + 2*b^2
m = 100000
isprime = prime_sieve(m)

def find_sol(n):
    for a in range(3,n):
        if isprime[a]:
            for b in range(1,n):
                r = a + 2*(b**2)
                if r > n: break
                if r == n: return
    verify(n)

for n in range(9, 10000000000, 2):
    if not isprime[n]:
        find_sol(n)

verify(1)
