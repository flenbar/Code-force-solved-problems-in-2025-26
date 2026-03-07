#flenbar
t = int(input())
for i in range(t):
    a , b , c , d = map(int,input().split())
    counts = 0
    if a > b:
        a , b = b , a
    if a < c < b:
        counts +=1
    if a < d < b:
        counts +=1
    if counts == 1:
        print("YES")
    else:
        print("NO")
