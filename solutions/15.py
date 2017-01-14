from math import *

def ways(n):
    return factorial(2*n)/(factorial(n)*factorial(n))

print(int(ways(20)))
