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
    return (primes, num)

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


def find_divisor(num, primes):
    p = 1
    for p in primes:
        if num%p==0:
            return p
    exit("bruh")

def is_prime(p):  # Lucas-Lehmer Test
    if p == 2:
        return True
    elif p <= 1 or p % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(p))+1, 2 ): 
            if p % i == 0: return False
        return True

primes, isPrime = sieve(30000)
def primeFactors(num):
    global primes, isPrime
    factors = []
    #primes, isPrime = sieve(num+1)

    while not is_prime(num):
        p = find_divisor(num, primes)
        factors.append(p)
        num = int(num/p)
    factors.append(num)
    return factors

def divisorCount(primes):
    a = {}
    for p in primes:
        if p in a:
            a[p] += 1
        else:
            a[p] = 2
    r = 1
    for k,i in a.items():
        r *= i
    return r
        

p = primeFactors(36)
print(p)
print(divisorCount(p))

def first():
    for t in Triangulars():
        if t < 20:
            continue
        divs = find_divisor(t)
        l = len(divs)
        print("%d %d" % (t, l))
        if l > 500:
            print(divs)
            break
def second():
    for t in Triangulars():
        if t < 20:
            continue
        ps = primeFactors(t)
        l = divisorCount(ps)
        print("%d %d" % (t, l))
        if l > 500:
            print(ps)
            print(t) #solution
            break


second()
