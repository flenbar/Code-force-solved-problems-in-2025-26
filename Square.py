#flenbar
t = int(input())
for i in range(t):
    c = []
    for j in range(4):
        a , b = map(int,input().split())
        c.append(a)
    d = list(set(c))
    print((abs(d[0]-d[1]))**2)
