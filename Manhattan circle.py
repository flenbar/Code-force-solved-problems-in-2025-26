#flenbar
t = int(input())
for i in range (t):
    a , b = map(int,input().split())
    x = 0
    y = 0
    counts = 0
    for j in range(1,a+1):
        n = input().strip()
        for k in range (b):
            if n[k] == "#":
                x += j
                y += k + 1
                counts += 1
    print(x//counts, y//counts)