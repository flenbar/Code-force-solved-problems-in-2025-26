#flenbar
t = int(input())
for i in range(t):
    r , b , d = map(int,input().split())
    e = r+b
    f = min(r,b)
    g = ((e - 1)//f)-1
    if  g <= d:
        print("YES")
    else:
        print("NO")
