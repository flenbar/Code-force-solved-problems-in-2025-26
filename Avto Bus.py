#flenbar
t = int(input())
for i in range(t):
    a = int(input())
    if a < 4 or a % 2 != 0:
        print(-1)
    else:
        if a <= 6:
            print(1,1)
        else:
            print((a+5)//6,a//4)
