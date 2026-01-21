n=int(input())
for i in range(n):
    b=input()
    c=b[0]
    for j in range (len(b)):
        if(b[j]==" " ):
            c+=b[j+1]
    print(c)
