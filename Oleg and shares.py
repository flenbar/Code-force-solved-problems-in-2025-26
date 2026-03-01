#flenbar
a , b = map(int,input().split())
c = list(map(int,input().split()))
z=c[0]%b
for i in c:
    if i%b!=z:
        print(-1)
        exit()
counts = 0
d = min(c)
for j in range(a):
    counts += (c[j]-d)//b
print(counts)
