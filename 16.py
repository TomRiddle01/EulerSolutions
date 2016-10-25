num = 2**1000
strings = list(str(num))
digits = [int(i) for i in strings]
print(sum(digits))
