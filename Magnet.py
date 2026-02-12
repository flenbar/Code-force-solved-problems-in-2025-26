a=int(input())
c=[]
for i in range(a):
    b=int(input())
    c.append(b)
counts=0    
for j in range(1,a):
    if(c[j]!=c[j-1]):
        counts+=1
print(counts+1)
