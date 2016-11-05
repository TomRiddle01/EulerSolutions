

i=1
f0 = 0
f1 = 1
f2=0
while len(str(f2))<1000:
    i+=1
    f2 = f0+f1
    f0 = f1
    f1 = f2


result = i
print(result)
import hashlib
print("a376802c0811f1b9088828288eb0d3f0")
print(hashlib.md5(str(result).encode('utf-8')).hexdigest())
