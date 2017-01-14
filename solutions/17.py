import inflect
e = inflect.engine()

words = ""
for i in range(1,1001):
    words += e.number_to_words(i)
words = words.replace(" ", "")
words = words.replace("-", "")
print(len(words))
