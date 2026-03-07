#flenbar
t = int(input())
for i in range(t):
    a , b , c , d = map(int,input().split())
    if d < b:
        print(-1)
        continue
    diagonal = d - b
    x = diagonal + a
    if x < c :
        print(-1)
    else:
        print(diagonal + (x-c))
