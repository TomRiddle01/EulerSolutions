import math
from itertools import *



def sieve(below):
    num = [True]*below
    num[0] = False
    num[1] = False
    primes = set(range(2,below))
    for (i, isprime) in enumerate(num):
        if isprime:
            for n in range(i*i, below, i):
                num[n] = False
                primes.discard(n)
    return primes


def findDivs(num):
    primes = sieve(int(num/2))
    divs = [p for p in primes if num%p==0]
    divs = set(divs)
    for prime in primes:
        if prime < math.sqrt(num):
            for f in count(2):
                if prime*f > num:
                    break
                elif num%(prime*f)==0:
                    divs.add(prime*f)

    return divs

class Triangulars:
    def __init__(self):
        self.i = 1
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        self.num += self.i
        return self.num


for t in Triangulars():
    if t < 20:
        continue
    divs = findDivs(t)
    l = len(divs)
    print("%d %d" % (t, l))
    if l > 500:
        print(divs)
        break

