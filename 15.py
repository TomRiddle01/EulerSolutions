from math import *

def ways(n):
    return factorial(2*n)/(factorial(n)*factorial(n))

print(ways(2))
print(ways(3))
print(ways(20))
    
