from Euler import *

i=1
f0 = 0
f1 = 1
f2=0
while len(str(f2))<1000:
    i+=1
    f2 = f0+f1
    f0 = f1
    f1 = f2


result = i
verify(result)
