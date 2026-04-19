#Flenbar
t = int(input())
for i in range(t):
    n = list(map(int,input().split()))
    n.sort()
    print(-1*((sum(n)-n[-1]))
          +n[-1])
