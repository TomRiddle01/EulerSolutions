import time
t = time.time()

def collatz_steps(n):
    steps = 0
    while n > 1:
        if n in powers_of_two:
            steps_to_one = powers_of_two.index(n)
            steps += steps_to_one
            n = 1
        else:
            if n%2 == 0:
                n = n/2
                steps += 1
            else:
                n = (3*n+1)/2
                steps += 2
    return steps


powers_of_two = [2**x for x in range(20)] #bis <1.000.000
print(powers_of_two)
n = 1000000
maxsteps = -1
maxnumber = -1
for i in range(1,n+1):
    steps = collatz_steps(i)
    if steps >= maxsteps:
        maxsteps = steps
        maxnumber = i


print("Die maximale Anzahl an Schritten einer Zahl <=",n," ist ",maxsteps,"mit der Zahl: ",maxnumber)
print("Berechnungszeit:",time.time()-t,"s")
