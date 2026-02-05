a=int(input())
for i in range(a):
    if(a%2!=0):
        print(-1)
        break
    else:
        if((i+1)%2==0):
            print(i,end=" ")
        else:
            print(i+2,end=" ") 