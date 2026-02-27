#flenbar
n , k = map(int,input().split())
a = list(map(int,input().split()))
counts = 0
for i in a:
    if i + k <= 5:
        counts += 1
print(counts // 3)