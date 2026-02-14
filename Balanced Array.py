#flenbar
t=int(input())
for i in range(t):
    n=int(input())
    if((n%2==0 and (n//2)%2!=0) or n%2!=0):
        print("NO")
    else:
        print("YES")
        c=[]
        for i in range(1,n+1):
            if(i%2==0):
                c.append(i)
        suma=sum(c)    
        for j in range(1,n-1):
            if(j%2!=0):
                c.append(j)
        sumb=sum(c)
        x=sumb-suma
        y=suma-x
        c.append(y)
        print(*c) 
