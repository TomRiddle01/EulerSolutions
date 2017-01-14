from Euler import *

def d(i):
    return set(int(x) for x in list(str(i)))

for i in range(1,100000000):
    ds = d(i)
    if all(ds == d(i*k) for k in range(2,6+1)):
        verify(i)
