from Euler import *
n = 1000000
isprime = prime_sieve(n)

ss = 0
for i in range(10,n):
    if isprime[i]:
        s = str(i)
        p = True
        for a in range(len(s)):
            if not isprime[int(s[a:])]:
                p = False
                break
            if not isprime[int(s[:(a+1)])]:
                p = False
                break
        if p:
            print(i)
            ss += int(i)
verify(ss)




