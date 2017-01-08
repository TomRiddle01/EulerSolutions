from Euler import *
from math import *

t = lambda n: 0.5*n*(n+1)
s = set()


def wordvalue(w):
    s = 0
    for c in list(w):
        s += ord(c)-64
    return s

ss = 0
with open("42_words.txt") as file:
    data = file.read()
    words = eval(data)

    for i in range(100):
        s.add(t(i))

    for w in words:
        if wordvalue(w) in s:
            ss+=1

verify(ss)
