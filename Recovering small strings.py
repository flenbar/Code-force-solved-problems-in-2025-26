#flenbar
t = int(input())
for i in range(t):
    x = "0abcdefghijklmnopqrstuvwxyz"
    n = int(input())
    if n <= 28:
        a = "aa"
        a += x[n-2]
        print(a)
    elif n <= 53:
        a = "a"
        a += x[n-27]
        a += "z"
        print(a)
    else:
        a = x[n-52]
        a += "zz"
        print(a)
