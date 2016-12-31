from itertools import *
import numpy

def isPrime(n):
    if n in primes:
        return True
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

prime = []
prime.append(False)
prime.append(False)
primes = []

i = 1
s = 0
while s < 1000000:
    if not i%1000:
        print(i)
    if isPrime(i):
        prime.append(True)
        primes.append(i)
        s += i
    else:
        prime.append(False)
    i += 1

primes_set = set(primes)

print("calculatted primes")
m = 0
r = 0
for a in range(len(primes)-21):
    for b in range(a+21,len(primes)):
        arr = primes[a:b]
        num = sum(arr)

        if num > 1000000:
            break

        if isPrime(num):
            if len(arr) > m:
                m = len(arr)
                r = num
                print(m,r)


print(m,r)
