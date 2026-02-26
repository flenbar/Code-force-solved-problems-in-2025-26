#flenbar
t = int(input())
for i in range(t):
    n, a, b, c, d = map(int, input().split())
    w = n * (a - b)
    x = n * (a + b)
    y = c - d
    z = c + d
    if x >= y and w <= z:
        print("YES")
    else:
        print("NO")
