#flenbar
t = int(input())
a = input().strip()
removed = 0
counter = 0
for i in a:
    if i == "x":
        counter += 1
        if counter > 2:
            removed += 1
    else:
        counter = 0
print(removed)
