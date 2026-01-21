n=int(input())
for i in range(n):
    x=int(input())
    b=list(map(int,input().split()))
    c=0
    for j in b:
        if(j>c):
            c=j
    print(c*x)        
