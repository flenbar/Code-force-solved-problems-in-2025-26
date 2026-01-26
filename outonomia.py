a=int(input())
for i in range(a):
    c=int(input())
    f=c-1
    counts=0
    d=list(map(int,input().split()))
    for j in range(f):
          h=d[j]-d[j+1]
          if h in (-7,-5,5,7):
              continue
          else:
              counts+=1
    if(counts==0):
        print("Yes")
    else:
        print("No") 