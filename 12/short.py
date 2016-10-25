from math import sqrt
n=1
a=1
m=2 # 1 and itself
while m<500:
    n+=1
    a+=n
    m=2
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            m+=2 # for found i there is a j: i*j==n
print(a)
