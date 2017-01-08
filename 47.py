from Euler import *

init_primes(1000000)

con = 0
for i in range(1,1000000):
    factors = set(prime_factors(i))
    if len(factors) == 4:
        con+=1
    else:
        con = 0
    if con == 4:
        verify(i-3)
        exit()
