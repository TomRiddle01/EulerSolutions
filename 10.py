import math
from itertools import *
import numpy

def isPrime(n):
    if n < 0:
        return False
    if n == 1:
        return True
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True

def nextPrime(n):
    for i in count(1):
        if isPrime(n+i):
            return n+i


def dropMultiples(l, num):
    for i in l:
        if i%num==0:
            l.remove(i)

def sieve(below):
    primes = []
    numbers = list(range(2,below))
    while True:
        p = numbers[0]
        primes.append(p)
        if p >= math.sqrt(below):
            break
        numbers = [x for x in numbers if x%p!=0]
        print(p)
    return set(primes).union(set(numbers))




print(sum(sieve(2000000)))
