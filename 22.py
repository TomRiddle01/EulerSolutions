#Problem 22
#==========
#
#
#   Using [1]names.txt, a 46K text file containing over five-thousand first
#   names, begin by sorting it into alphabetical order. Then working out the
#   alphabetical value for each name, multiply this value by its alphabetical
#   position in the list to obtain a name score.
#
#   For example, when the list is sorted into alphabetical order, COLIN, which
#   is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
#   COLIN would obtain a score of 938 × 53 = 49714.
#
#   What is the total of all the name scores in the file?
#
#
#   Visible links
#   1. names.txt
#   Answer: f2c9c91cb025746f781fa4db8be3983f


with open('22_names.txt', 'r') as myfile:
        names=myfile.read().replace('\n', '')

names = eval("["+names+"]")
names = sorted(names)

def word(w):
    s = 0
    for c in w:
        s += ord(c)-64
    return s

result = 0
for i,name in enumerate(names,1):
    result += i*word(name)

print(result)
