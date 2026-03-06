#flenbar
t = int(input())
for i in range(t):
    n = input().strip()
    for j in range(len(n)-1):
        if n[j] == n[j+1]:
            print(1)
            break
    else:
        print(len(n))
