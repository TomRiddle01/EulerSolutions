from Euler import *

#isprime = prime_sieve(999999999) # maximum possible, but is to large
isprime = prime_sieve(8000000) # maximum necessary

nums = ["1","2","3","4","5","6","7","8","9"]
largest = 0
for i, p in enumerate(isprime):
    if p:
        s = str(i)
        l = len(s)
        se = set(list(s))
        if se == set(nums[:l]):
            largest = i

verify(largest)

