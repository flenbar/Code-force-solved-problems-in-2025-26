#flenbar
a = int(input())
b = list(map(int, input().split()))
neg = 0
zero = 0
cost = 0
for x in b:
    if x < 0:
        cost += abs(x + 1)
        neg += 1
    elif x > 0:
        cost += abs(x - 1)
    else:
        cost += 1
        zero += 1
if neg % 2 != 0 and zero == 0:
    cost += 2
print(cost)
