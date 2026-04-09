#flenbar
t = int(input())
for i in range(t):
    s = input()
    num1 = 0
    num2 = 0
    for j in range(6):
        if j < 3:
            num1 += int(s[j])
        else:
            num2 += int(s[j])
    if num1 == num2:
        print("YES")
    else:
        print("NO")
