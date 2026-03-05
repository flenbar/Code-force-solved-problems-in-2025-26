#flenbar
t = int(input())
for i in range(t):
    a , b = map(int,input().split())
    x = list(map(int,input().split()))
    e = "".join(map(str, x))
    first = e.find("1")
    last = e.rfind("1")
    d =e[first:last+1]
    if len(d) <= b:
        print("YES")
    else:
        print("NO")
