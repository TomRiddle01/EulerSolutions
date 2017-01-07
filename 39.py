from Euler import *

m = 120

rm = 0
rr = 0
for m in range(1,1001):
    sols = 0
    for a in range(1, m):
        for b in range(1, m-a):
            c = (m-a-b)
            if a**2 + b**2 == c**2:
                sols += 1

    if rr < sols:
        rm = m
        rr = sols
verify(rm)


