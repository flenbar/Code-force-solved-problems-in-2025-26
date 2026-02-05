a= int(input())
for i in range(a):
    c="ABCDEFG"
    n,m=map(int,input().split())
    b=input()
    sums=0
    for j in range(7):
        d=b.count(c[j])
        e=m-d
        if((m-d)>=0):
            sums+=e
    print(sums)