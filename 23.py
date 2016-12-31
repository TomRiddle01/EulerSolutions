from saver import *

def abundant(n):
    divsum = 1
    for i in range(2,int(n/2)):
        if n%i == 0:
            divsum += i
        if n < divsum:
            return True
    return False


save(2)
exit()
abundants = {}
for i in range(28123):
    abundants[i] = abundant(i)



limit = 28123
for i in range(limit, 0, -1):
    #print(i)
    pass
print("done")





