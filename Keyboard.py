#flenbar 
c = input()
a = input()
b = "qwertyuiopasdfghjkl;zxcvbnm,./"
s =""
for i in range (len(a)):
    if c == "R":
        d = b.index(a[i])-1
        s += b[d]
    else:
        d = b.index(a[i])+1
        s += b[d]
print(s)        
