from itertools import *
import numpy
from Euler import * 

isprime = prime_sieve(1000000)
primes = [i for i,p in enumerate(isprime) if p]


m = 21
r = 0
for a in range(len(primes)-21):
    if a*m > 1000000:
        break
    for b in range(m,len(primes)):
        arr = primes[a:a+b]
        num = sum(arr)

        if num >= 1000000:
            break

        if isprime[num]:
            if len(arr) > m:
                m = len(arr)
                r = num
verify(r)
