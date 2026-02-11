a=int(input())
counts=0
for j in range(a):
    b=list(map(int,input().split()))
    c=b.count(1)
    if(c>=2):
        counts+=1
print(counts)