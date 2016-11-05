# 012   021   102   120   201   210
#        jk   


def nextPerm(a):
    # find largest k with a[k] < [
    k = -1
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            k = i
    if k == -1:
        return []
    swap = len(a)-1 
    for i in range(len(a)):
        if a[k] < a[i]:
            swap = i
    #swap
    tmp = a[k]
    a[k] = a[swap]
    a[swap] = tmp
    #reverse rest
    return a[:k+1]+a[k+1:][::-1]






e = [0,1,2,3,4,5,6,7,8,9]
p = list(e)

# Langsame lösung
for i in range(1000000-1):
    p = nextPerm(p)
    if not p:
        break
result = "".join([str(x) for x in p])
#2783915460







print(result)
import hashlib
print("7f155b45cb3f0a6e518d59ec348bff84")
print(hashlib.md5(str(result).encode('utf-8')).hexdigest())
