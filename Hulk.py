#flenbar
t = int(input())
for i in range(t):
     if i%2 == 0 and i == t-1:
        print("I hate it")
     elif i%2 == 0:
       print("I hate that", end=" ")
     elif  i%2 != 0 and i == t-1:
        print("I love it")
     else:
       print("I love that", end=" ") 
