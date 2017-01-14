from Euler import *

isprime = prime_sieve(100000)

m = 10000
for t1 in range(1487+1, m):
    if isprime[t1]:
        for n in range(1,m//2):
            t2 = t1+n
            t3 = t1+n*2
            if isprime[t2] and isprime[t3]:
                s1 = list(str(t1))
                s1.sort()
                s2 = list(str(t2))
                s2.sort()
                s3 = list(str(t3))
                s3.sort()
                if s1 == s2 and s2 == s3:
                    print(t1, t1+n, t1+n*2)
                    verify("%d%d%d" % (t1,t2,t3))
