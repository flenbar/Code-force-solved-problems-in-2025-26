#flenbar
k, n, w = map(int,input().split())
kk = 0
for i in range(w):
    kk += (i+1)*k
if kk <= n:
    print(0)
else:
    print(kk-n)    