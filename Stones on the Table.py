n=int(input())
s=input().strip()
counts=0
for i in range(1,n):
    if(s[i]==s[i-1]):
        counts+=1
print(counts)        
