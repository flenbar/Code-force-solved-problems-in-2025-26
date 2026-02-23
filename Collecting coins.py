#flenbar
t = int(input())
for i in range(t):
    a, b, c, n = map(int, input().split())
    maxi = max(a, b, c)
    need = (maxi - a) + (maxi - b) + (maxi - c)
    if n < need:
        print("NO")
    else:
        if (n - need) % 3 == 0:
            print("YES")
        else:
            print("NO")
