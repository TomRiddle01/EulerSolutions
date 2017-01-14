from itertools import *
import numpy
from Euler import *

def nextPrime(n):
    for i in count(1):
        if is_prime(n+i):
            return n+i

p = 0
#for i in range(0, 10001+1):
#    p = nextPrime(p)

isprime = prime_sieve(1000000)

i = 0
pi = 0
while True:
    if isprime[i]:
        pi+=1
    if pi == 10001:
        verify(i)
    i+=1
        

