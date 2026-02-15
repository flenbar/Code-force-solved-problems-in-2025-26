#flenbar
t=int(input())
for i in range(t):
    a = int(input())
    temp=a               
    b=str(a)
    c=10**(len(b)-1)     
    counts=0
    z=[]
    while c>0:
        digit=temp//c     
        if digit!=0:
            part=digit * c
            z.append(part)
            counts+=1
        temp=temp%c
        c//=10
    print(counts)
    print(*z)
