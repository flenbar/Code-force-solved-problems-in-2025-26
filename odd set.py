 n=int(input())
for i in range(n):
    b=int(input())
    c=list(map(int,input().split()))
    d=0
    e=0
    for j in c:
        if(j%2==0):
            d+=1
        if(j%2!=0):
            e+=1
        
    if(d==b and e==b):
        print("yes")
    else:
        print("No")   
