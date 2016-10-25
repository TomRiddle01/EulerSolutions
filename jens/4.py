def is_palindrome(zahl):
    zahl = str(zahl)
    zahl_liste = []
    for i in zahl:
        zahl_liste.append(i)
    if zahl_liste == zahl_liste[::-1]:
        return True
    else:
        return False

palindrom_liste = []
for x in range(100,1000):
    for y in range(100,1000):
        if is_palindrome(x*y):
            #palindrom_liste.append([x,y,x*y])
            pass
print(palindrom_liste)
