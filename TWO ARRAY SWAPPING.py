x = int(input())
for _ in range(x):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)

    for i in range(min(k, n)):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    print(sum(a))    