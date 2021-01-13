import string
#its not week 5 task but i got a bit of issue with my file so i just put it there
f = open("C://BINUS PROGRAM/week 5 task/demoo.txt","r")
txt = f.read().lower().replace("\n","")
newtxt = ""
for c in txt:
    if c not in string.punctuation:
        newtxt += c
txt = newtxt
lst = txt.split(" ")
d = {}
for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
newd = []
for i in d:
    if d[i] == 1:
        newd.append(i)
print("Hapax in the text")
for word in newd:
    print(word)
