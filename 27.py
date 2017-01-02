from Euler import *

def getFormula(a,b):
    return lambda n: n*n + a*n + b

isprime = prime_sieve(87400)
m = 0
ma = 0
mb = 0
for a in range(-999, 1000, 2): # a has to be odd
    for b in range(-1000, 1000):
        if not isprime[abs(b)]: # idea from forum
            continue
        f = getFormula(a,b)
        if not isprime[f(40)]:
            continue
        i = 1
        while isprime[f(i)]:
            i+=1
        if i > m:
            m = i
            ma = a
            mb = b

print(m)
print(ma)
print(mb)
verify(ma*mb)
