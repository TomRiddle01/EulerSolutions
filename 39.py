from Euler import *

m = 120

rm = 0
rr = 0
for m in range(1,1000):
    sols = 0
    for a in range(1, m):
        for b in range(1, m-a):
            c = (m-a-b)
            aabb = a*a + b*b
            cc = c*c
            if cc < aabb: break
            if aabb == cc:
                sols += 1

    if rr < sols:
        rm = m
        rr = sols
verify(rm)


