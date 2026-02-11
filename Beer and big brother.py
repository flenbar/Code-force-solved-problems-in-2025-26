a,b=map(int,input().split())
counts=0
while(a<=b):
    a*=3
    b*=2
    counts+=1
print(counts)
