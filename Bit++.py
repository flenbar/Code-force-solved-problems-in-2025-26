#flenbar
t = int(input())
total = 0
for i in range(t):
    s = input().strip()
    if s == "++X" or s == "X++":
        total += 1
    if s == "--X" or s == "X--":
        total -= 1
print(total)        
        
