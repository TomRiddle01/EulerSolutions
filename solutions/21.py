
 #  Let d(n) be defined as the sum of proper divisors of n (numbers less than
 #  n which divide evenly into n).
 #  If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
 #  and each of a and b are called amicable numbers.

 #  For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
 #  44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
 #  2, 4, 71 and 142; so d(284) = 220.

 #  Evaluate the sum of all the amicable numbers under 10000.

 # Answer: 51e04cd4e55e7e415bf24de9e1b0f3ff
from math import *
def findDivsum(n):
    divsum = 0 
    for i in range(1,n):
        if n%i==0:
            divsum += i
    return divsum

amic = dict()
ss=0
for i in range(10000):
    a = i
    b = findDivsum(a)
    a_ = findDivsum(b)
    if a == a_ != b:
        ss+=a
        print(a,b)


print(ss)
