x = int(input())
for i in range(x):
    a=input().strip()
    b=input().strip()
    c=[]
    for j in range(len(b)):
        d=a.index(b[j])
        c.append(d)
    sums=0    
    for k in range(1,len(c)):
        sums+=abs(c[k]-c[k-1])
    print(sums)    