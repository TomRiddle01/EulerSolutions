i0 = 0
i1 = 1
s = 0
for i in range(0, 1000000000000):
    f = i1+i0
    i0=i1
    i1= f
    if f >= 4000000:
        break
    if f%2==0:
        s += f

print(s)
