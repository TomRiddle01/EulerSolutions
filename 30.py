from Euler import verify

ss = 0
for i in range(2,999999):
    s = sum(int(x)**5 for x in list(str(i)))
    if s == i:
        print(s)
        ss+=s
verify(ss)
