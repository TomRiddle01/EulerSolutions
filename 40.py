from Euler import *

d = " "

for i in range(1,200000):
    d += str(i)

verify(int(d[1])*int(d[10])*int(d[100])*int(d[1000])*int(d[10000])*int(d[100000])*int(d[1000000]))
