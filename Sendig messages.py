#flenbar
t = int(input())
for i in range(t):
    n, f, a, b = map(int, input().split())
    x = list(map(int, input().split()))
    y = 0
    for j in x:
        w = j - y
        z = min(w * a, b)
        
        f -= z
        y = j
    if f > 0:
        print("YES")
    else:
        print("NO")
    
