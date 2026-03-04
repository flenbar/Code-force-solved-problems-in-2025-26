#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(set(a))
    if a.count(b[0]) < a.count(b[1]):
        print(a.index(b[0])+1)
    else:
        print(a.index(b[1])+1)
