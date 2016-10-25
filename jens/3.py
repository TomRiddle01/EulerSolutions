#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 60085475143 ?
from math import ceil,sqrt

def is_prime(p):  # Lucas-Lehmer Test
    if p == 2:
        return True
    elif p <= 1 or p % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(p))+1, 2 ): 
            if p % i == 0: return False
        return True

zahl = 600851475143
n = zahl
prime = []
i = 1
while not is_prime(n):
    i += 1
    if is_prime(i):
        print("%d, %d"%(i,n%i))
        if n % i == 0:
            prime.append(i)
            n = int(n/i)
            print(n)
            i = 1
prime.append(n)
max_prime = n

print(prime)
print("Der größte Primfaktor von",zahl,"ist",max_prime)
