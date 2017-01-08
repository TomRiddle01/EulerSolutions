from Euler import *

T = lambda n: n*(n+1)/2
P = lambda n: n*(3*n-1)/2
H = lambda n: n*(2*n-1)

Ts,Ps,Hs = set(),set(),set()

for i in range(144,100000): # estimated
    Ts.add(T(i))
    Ps.add(P(i))
    Hs.add(H(i))

for t in Ts:
    if t in Ps and t in Hs:
        verify(t)



