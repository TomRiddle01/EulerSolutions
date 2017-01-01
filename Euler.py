

primes = set()
learned_primes = 0

# Lucas Lehmer Test
def is_prime(n):
    if n in primes:
        return True
    if n <= 0:
        return False
    if n == 1:
        primes.add(n)
        return True
    for i in range(2,n-1):
        if n%i==0:
            return False
    primes.add(n)
    return True


def find_divisor(num):
    for i in range(learned_primes, num+1):
        is_prime(i)

    p = 1
    for p in primes:
        if p <= 1:
            continue
        if num%p==0:
            return p
    raise Exception("primes array not initialized")

def prime_factors(num):
    factors = []

    while not is_prime(num):
        p = find_divisor(num)
        factors.append(p)
        num = int(num/p)
    factors.append(num)
    return factors

def div_count(n):
    for i in range(learned_primes, n+1):
        is_prime(i)
    factors = prime_factors(n)
    a = {}
    for p in factors:
        if p in a:
            a[p] += 1
        else:
            a[p] = 2
    r = 1
    for k,i in a.items():
        r *= i
    return r


def div_sum(n):
    divsum = 0 
    for i in range(1,n):
        if n%i==0:
            divsum += i
    return divsum

def div_sum(n):
    divsum = 0 
    for i in range(1,n):
        if n%i==0:
            divsum += i
    return divsum
