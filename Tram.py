#flenbar
t = int(input())
maxi = 0
c = 0
for i in range (t):
     a , b = map(int,input().split())
     c  += (b - a)
     if c >= maxi:
         maxi = c
print(maxi)       
