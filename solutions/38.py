from Euler import *

e = set([1,2,3,4,5,6,7,8,9])

m = 0
for n in range(1, 5): # 5 because len("aa"+"bb"+"cc"+"dd"+"ee") > 9 
    f = list(range(1,n))
    for i in range(9, 10000):
        pcon = "".join(str(x*i) for x in f)
        if len(pcon) > 10: break
        if len(pcon) == 9:
            digit_set = set(int(s) for s in list(pcon))
            if digit_set == e:
                mi = int(pcon)
                if mi > m:
                    m = mi
verify(m)
