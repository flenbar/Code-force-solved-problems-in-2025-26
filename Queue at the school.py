#flenbar            
a,b=map(int,input().split())
c=input().strip()
d=list(c)
for j in range(b):
    k=1
    while k < len(d):
        if d[k] == "G" and d[k-1] == "B":
            d[k],d[k-1]=d[k-1],d[k]
            k+=2
        else:
            k+=1
print("".join(d))