from itertools import *
from math import *
from Euler import *

# ~5 sec
#for a in range(1000):
#    for b in range(a,1000-a):
#        for c in range(b,1000-b):
#            if a+b+c == 1000:
#                if a**2+b**2 == c**2:
#                    print("%s, %s, %s"%(a,b,c))
#                    print("%s"%(a*b*c))
#                    verify(a*b*c)

# ~ 0.092 sec
#starting with c because c is the largest and MUST be over 10
# omitted loop over a because we can just use use the pythagorean theorem if we have c and b
for c in range(10, 1000):
    for b in range(10,c):
        a = int(sqrt(c**2-b**2))
        if a+b+c == 1000:
            if a**2+b**2 == c**2:
                print("%s, %s, %s"%(a,b,c))
                print("%s"%(a*b*c))
                verify(a*b*c)
