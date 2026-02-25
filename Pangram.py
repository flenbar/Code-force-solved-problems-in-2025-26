#flenbar
n = int(input())
s = input().strip().lower()
a = set(s)
if len(a) == 26:
    print("YES")
else:
    print("NO")
