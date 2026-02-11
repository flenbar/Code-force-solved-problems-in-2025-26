n,h=map(int,input().split())
a=list(map(int,input().split()))
c=[]
for i in range(n):
    if(a[i]>h):
        c.append(2)
    else:
        c.append(1)
print(sum(c))        
        
