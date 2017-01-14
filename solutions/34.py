from Euler import *
from math import *

ss = 0
for i in range(3,100000):
    fs = sum(factorial(int(s)) for s in str(i))
    if i == fs:
        ss += i

verify(ss)
