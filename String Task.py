#flenbar
a = input().strip()
b = a.lower()
c = "."
d = "aoyeui"
for i in b:
    if i not in d:
        c += i
        c += "."
print(c[:-1])