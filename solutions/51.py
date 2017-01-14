from Euler import *
from itertools import *

m = 1000000
isprime = prime_sieve(m)


def prime_family(num_, wildcards, b = False):
    num = list(str(num_))
    n = 0
    for i in range(10):
        for w in wildcards:
            num[w] = str(i)
        if num[0] != "0" and isprime[int("".join(num))]:
            if b: 
                return "".join(num)
            n += 1
    return n



for p in range(1001,m, 2):
    for r in [3,4,5,6]:
        for wildcards in combinations(range(len(str(p))), r):
            if 8 == prime_family(str(p), wildcards):
                pp = list(str(p))
                for w in wildcards:
                    pp[w] = "_"
                verify(prime_family(str(p), wildcards, True))
