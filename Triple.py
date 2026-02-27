#flenbar
t = int(input())
for i in range (t):
    n = int(input())
    a = list(map(int,input().split()))
    counts = {}
    for j in a:
        counts[j] = counts.get(j,0) + 1
        if counts[j] >= 3:
            print(j)
            break
    else:        
        print(-1)