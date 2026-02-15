#flenbar
a=input().strip()
b=""
i=0
while i < len(a):
    if a[i]=="-":
        if a[i+1]=="-":
            b+="2"
            i+=2
        else:
            b+="1"
            i+=2
    else:
       b+="0"
       i+=1
print(b)
 
