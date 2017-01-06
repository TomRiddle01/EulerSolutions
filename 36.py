from Euler import *

s = 0
def palin(n):
    n = str(n)
    if len(n)%2 == 0:
        return n[len(n)//2:] == n[:len(n)//2][::-1]
    else:
        return n[len(n)//2:] == n[:len(n)//2+1][::-1]

for i in range(1000000+1):
    if palin(i) and palin(bin(i)[2:]):
        s += i
verify(s)
