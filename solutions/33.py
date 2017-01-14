from Euler import *

r = []
ar = 1
br = 1
def same(a,b,a2,b2,o1,o2):
    global ar, br
    if o1 == "0": return
    if o2 == "0": return
    if b2 == "0": return
    if a/b == int(a2)/int(b2):
        r.append((a,b))
        ar *= a
        br *= b

for a in range(10, 100):
    for b in range(a+1,100):
        a_s = str(a)
        b_s = str(b)
        if a_s[0] == b_s[0]: same(a,b, a_s[1], b_s[1], a_s[0], b_s[0])
        if a_s[0] == b_s[1]: same(a,b, a_s[1], b_s[0], a_s[0], b_s[1])
        if a_s[1] == b_s[0]: same(a,b, a_s[0], b_s[1], a_s[1], b_s[0])
        if a_s[1] == b_s[1]: same(a,b, a_s[0], b_s[0], a_s[1], b_s[1])

print(ar)
print(br)

shortened = True
while shortened:
    shortened = False
    for i in range(2,min(ar,br)+1):
        if ar%i==0 and br%i==0:
            ar = ar//i
            br = br//i
            shortened = True

print(ar)
print(br)
verify(br)
