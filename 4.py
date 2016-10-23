from itertools import *

def is6Palindrome(i):
    s = str(i)
    if len(s) == 6 and s[:3]==s[-3:][::-1]:
        return True
    return False


l = 111*111
for x,y in product(range(111,999), range(111,999)):
    if is6Palindrome(x*y):
        l = max(l, x*y)

print(l)

