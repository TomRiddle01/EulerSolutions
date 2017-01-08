from Euler import *

P = lambda n: n*(3*n-1)/2

Ps = set()


l = 5000 # estimated
for i in range(1,l):
    Ps.add(P(i))

for a in Ps:
    for b in Ps:
        if a+b in Ps:
            if b-a in Ps:
                verify(abs(a-b))

