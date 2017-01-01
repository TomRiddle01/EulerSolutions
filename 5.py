from itertools import *
import math
import numpy
from EulerVerify import verify

# ca 1.6 - 2.0s
def findSmallest():
    for i in range(1,20):
        for p in combinations(range(1,20), i):
            n = numpy.prod(p)
            if max([n%x for x in range(1,20)])==0:
                print(p)
                return n


def findSmallest():
    relevant = [2,3,4,5,11,12,13,14,15,16,17,18,19,20]
    for i in range(3,20):
        for p in combinations(relevant, i):
            n = numpy.prod(p)
            if max([n%x for x in range(1,20)])==0:
                print(p)
                return n


verify(findSmallest())
