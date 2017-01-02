from Euler import *


def divide1by(n, depth):
    digits = []
    h = 10
    for s in range(depth):
        d = h//n
        #h = (h-(d*n))*10
        h = (h%n)*10
        digits.append(d)
        if h == 0:
            break
    return digits

def getCycle(digits, startlength):
    for s in range(len(digits)):
        for l in range(startlength, int((len(digits)-s)/2)+1):
            r = int((len(digits)-s)/l)
            seg = digits[s:s+l]
            equal = True
            for i in range(r):
                if seg != digits[s+i*l:s+l+i*l]:
                    equal = False
                    break
            if equal:
                return seg
    return []



#print(getCycle(divide1by(983,10000),1))


depth = 10000
m = 6
mi = None
ma = None
isprime = prime_sieve(1000000)
for i in range(1, 1000):
    if not isprime[i]: # as i've learned it seems only 1/prime has a periodic fraction part
        continue
    digits = divide1by(i,depth)
    if len(digits) <= m:
        continue
    cycle = getCycle(digits, 1)
    if i == 997:
        print(len(cycle))
    if len(cycle) > m:

        m = len(cycle)
        mi = i
        md = digits

verify(mi)
