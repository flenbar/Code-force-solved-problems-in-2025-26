#flenbar
a, b, c = map(int,input().split())
if a > c:
    if a%c == 0:
        x = a//c
    else:
        x = a + (c - a%c)
        x //=c
else:
    x = 1    
if b > c:
    if b%c == 0:
        y = b//c
    else:
        y = b + (c - b%c) 
        y //=c
else:
    y = 1
print(x*y)