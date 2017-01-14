from Euler import *
from itertools import *

i = 0
for d1,d2,d3,d4,d5,d6,d7,d8,d9,d10 in permutations(["0","1","2","3","4","5","6","7","8","9"]):
    if int(d4)%2 == 0:
        if int(d3+d4+d5) % 3 == 0:
            if int(d4+d5+d6) % 5 == 0:
                if int(d5+d6+d7) % 7 == 0:
                    if int(d6+d7+d8) % 11 == 0:
                        if int(d7+d8+d9) % 13 == 0:
                            if int(d8+d9+d10) % 17 == 0:
                                i += int(d1+d2+d3+d4+d5+d6+d7+d8+d9+d10)


print(i)
