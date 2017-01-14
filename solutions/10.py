import math
from itertools import *
import numpy
from Euler import *

isprime = prime_sieve(2000000)
primes = [i for i,p in enumerate(isprime) if p]
verify(sum(primes))
