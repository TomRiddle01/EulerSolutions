from Euler import *

collatz = {}
def collatz_len(n):
    if n == 1:
        return 1
    if n in collatz:
        return collatz[n]
    else:
        if n % 2 == 0:
            nn = n//2
            l = collatz_len(nn)
            mem(nn,l)
            return 1+l
        else:
            nn = 3*n+1
            l =  collatz_len(nn)
            mem(nn,l)
            return 1+l

def mem(n,l):
    collatz[n] = l

starting = 0
maximum = 0
for n in range(1,1000000, 1):
    l = collatz_len(n)
    if l > maximum:
        maximum = l
        starting = n
print("%d: %d"%(starting, maximum))
verify(starting)
