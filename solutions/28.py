from Euler import *



def inner(n):
    if n == 1: return 0
    return (n-2)**2 

br = lambda n: inner(n)+n-1
ur = lambda n: inner(n)+2*n


i = 2
s = 1
l = 0
for n in range(3,1001+1, 2): # only uneven steps necessary
    l+=1
    print("n",n)
    #s += i+(n-2)
    #s += i+(n-2)+(n-1)
    #s += i+(n-2)+(n-1)+(n-1)
    #s += i+(n-2)+(n-1)+(n-1)+(n-1)
    s += 4*i + 10*n - 14
    i += 4*(n-1)

verify(s)
