from itertools import *
import math
import numpy



n = 100+1
print(sum(range(1,n))**2 - sum(x**2 for x in range(1,n)))
