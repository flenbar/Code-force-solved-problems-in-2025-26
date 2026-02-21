#flenbar
t = int(input())
n = str(t).strip()
c =str( n.count("4") + n.count("7")).strip()
if c == "4" or c == "7":
    print("YES")
else:
    print("NO")
