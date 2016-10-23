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


def find_divisor(num):
    p = 1
    while p < num:
        p = nextPrime(p)
        if num%p==0:
            return p
    exit("bruh")

def primeFactors(num):
    factors = []

    while not isPrime(num):
        p = find_divisor(num)
        factors.append(p)
        num = int(num/p)
    factors.append(num)
    return factors



num = 600851475143

result = primeFactors(num)
print("For num=%d"%num)
print(result)
print("Largest: %d" % max(result))
print("Test: %d" % numpy.prod(result))
