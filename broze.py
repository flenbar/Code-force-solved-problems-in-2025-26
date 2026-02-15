#ismael
a=input().strip()
b=""
i=0
while (i <= len(a) and a[-1]!="." ) or i<=len(a)+1:
    if a[i]=="-":
        if a[i+1]=="-":
            b+="2"
            i+=2
            if i==len(a):
                break
        else:
            b+="1"
            i+=2
            if i==len(a):
                break
    else:
       b+="0"
       i+=1
       if i == len(a):
           break
