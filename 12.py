

def triangle(i):
    return sum(range(1,i+1))

def findDivisors(k):
    return [i for i in range(1,k+1) if k%i==0]




for i in range(0,1000000000000000):
    l = len(findDivisors(triangle(i)))
    if l > 500:
        print(i)
        break

