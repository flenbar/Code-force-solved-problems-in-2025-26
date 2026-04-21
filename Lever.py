#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = 0
    for k in range(n):
        if a[k] > b[k]:
            ans += (a[k] - b[k])
    print(ans+1)        
