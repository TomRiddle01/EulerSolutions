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

p = 0
for i in range(0, 10001+1):
    p = nextPrime(p)
    #print("p(%d) = %d"%(i,p))
print(p)



