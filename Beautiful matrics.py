for i in range(5):
    c=list(map(int,input().split()))
    for j in range(5):
        if (c[j]==1):
            row=i+1
            column=j+1
print(abs(row-3)+abs(column-3))
