from itertools import *
import math
import numpy

def findSmallest_wrong():
    for i in count(1):
        k = [i%x for x in range(1,20)]
        print(k)
        if max([i%x for x in range(1,20)])==0:
            return i

def findSmallest():
    for i in range(1,20):
        for p in combinations(range(1,20), i):
            n = numpy.prod(p)
            if max([n%x for x in range(1,20)])==0:
                print(p)
                return n


print(findSmallest())
