#flenbar
import math
a = "314159265358979323846264338327"
t = int(input())
for i in range(t):
    counts = 0
    b = input().strip()
    for i in range (len(b)):
        if b[i] == a[i]:
            
            counts += 1
        else:
            break
    print(counts)
