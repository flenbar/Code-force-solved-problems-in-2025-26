#flenbar
t = int(input())
for i in range(t):
    n = int(input())
    s = input().strip()
    first = s.find('B')
    last = s.rfind('B')
    print(last-first+1)
