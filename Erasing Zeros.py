#flenbar
t = int(input())
for i in range(t):
    b = input().strip()
    left = b.find("1")
    right = b.rfind("1")
    c = b[left:right+1]
    print(c.count("0"))
