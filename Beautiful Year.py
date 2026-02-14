#flenbar
y=int(input())
while True:
    s=""
    y+=1
    s+=str(y)
    d=set(s)
    if(len(s)==len(d)):
        print(y)
        break
