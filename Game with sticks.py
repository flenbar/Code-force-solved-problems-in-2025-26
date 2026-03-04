#flenbar
a , b = map(int,input().split())
counts = 0
for i in range(min(a,b)):
    if a == 1 or b == 1:
        break
    else:
        counts += 1
        a -= 1
        b -= 1
        
if counts %2 != 0:
    print("Malvika")
else:
    print("Akshat")
