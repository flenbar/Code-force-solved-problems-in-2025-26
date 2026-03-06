#flenbar
t = int(input())
for j in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    sums = 0
    for i in range(n):
        sums += abs(a[i])
    print(sums)