from itertools import *
from math import *

for a in range(1000):
    for b in range(a,1000-a):
        for c in range(b,1000-b):
            if a+b+c == 1000:
                if a**2+b**2 == c**2:
                    print("%s, %s, %s"%(a,b,c))
                    print("%s"%(a*b*c))
