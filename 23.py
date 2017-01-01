from saver import *
import itertools

s = Saver()
#s.ignore()

limit = 28123
# calculated
limit = 20162

def abundant(n): # this could work faster but i dont wont to copy the whole algorithm :p
    divsum = 1
    for i in range(2,int(n)):
        if n%i == 0:
            divsum += i
        if n < divsum:
            return True
    return False

abundants = s.load("abun")
if abundants == None:
    abundants = list()
    for i in range(limit+1):
        if abundant(i):
            abundants.append(i)
    s.save("abun", abundants)

r_abundants = abundants[::-1]

def find_pair(a1, s):
    for a2 in r_abundants:
        if a1+a2 < s:
            return False
        if a1+a2 == s:
            print(a1,"+", a2, "=", s)
            return True

    return False


# Solution hardly inspired by http://blog.dreamshire.com/project-euler-23-solution/
# Precalculation the abundants was stupid
# Also i didn't realize that i can use the implication as it was used there
# a in abn
# forall b: (b-a) not in abn
# => b is summable
abn = set()
s = 0
for i in range(20161+1):
    print(i)
    if abundant(i):
        abn.add(i)
    if not any( (i-a in abn) for a in abn):
        s += i

print(s)







