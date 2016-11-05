# 012   021   102   120   201   210
#        jk   

e = [1,2,3,4]
a = list(e)

i = len(a)-1
while a != list(e[::-1]):
    if i == 0:
        i = len(a)-1
        continue

    j = a[i-1]
    k = a[i]
    if j<k: # tausche ziffern
        a[i-1] = k
        a[i] = j
        i -= 1
    else:
        del a[i-1]
        a.append(j)
        i = len(a)-1
    print(a)



result =0
print(result)
import hashlib
print("7f155b45cb3f0a6e518d59ec348bff84")
print(hashlib.md5(str(result).encode('utf-8')).hexdigest())
