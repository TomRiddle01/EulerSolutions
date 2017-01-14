from Euler import *
from math import *


def ncr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

s = 0
for n in range(1,101):
    for r in range(1,n+1):
        if ncr(n,r) > 1000000:
            s += 1

verify(s)
