def seq(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

class Sequence:
    def __init__(self, start):
        self.v = start

    def __iter__(self):
        return self

    def __next__(self):
        self.v = seq(self.v)
        return self.v


starting = 0
maximum = 0
for i in range(1,1000000):
    l = [i]
    for x in Sequence(i):
        l.append(x)
        if x == 1:
            break # next sequence
    num = len(l)
    if num > maximum:
         starting = i
         maximum = num
    #print("%d: %d"%(i,maximum))

print("%d: %d"%(starting, maximum))