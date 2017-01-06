from Euler import *
s = set(["1","2","3","4","5","6","7","8","9"])

su  = set()
# 9999 is estimated maximum
for a in range(1, 9999):
    for b in range(1, 9999):
        digits = list(str(a)+str(b)+str(a*b))
        if len(digits) > 9: break
        if set(digits) == s:
            su.add(a*b)

verify(sum(su))
