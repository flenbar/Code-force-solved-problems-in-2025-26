n = int(input())
for  i in range(n):
    a , b , c = map(int , input().split())
    if a > b:
        print("First")
    elif b > a:
        print("Second")
    else:
        if c%2==1:
            print("First")
        else:
            print("Second")
