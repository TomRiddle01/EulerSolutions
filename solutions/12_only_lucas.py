import math
from itertools import *



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



def is_prime(p):  # Lucas-Lehmer Test
    if p == 2:
        return True
    elif p <= 1 or p % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(p))+1, 2 ): 
            if p % i == 0: return False
        return True





def find_divisor(num):
    p = 1
    for p in count(2):
        if is_prime(p):
            if num%p==0:
                return p
    exit("bruh")


def primeFactors(num):
    factors = []

    while not is_prime(num):
        p = find_divisor(num)
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

def find():
    for t in Triangulars():
        if t < 20:
            continue
        ps = primeFactors(t)
        l = divisorCount(ps)
        #print("%d %d" % (t, l))
        if l > 500:
            print("Alle Vielfache von:"+str(ps))
            break


find()
