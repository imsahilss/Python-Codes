t = int(input(''))
while t > 0:
    n = int(input(''))
    a = list(map(int, input().split()))
    x = []
    f = 0
    if a[0]>a[1]:
        x.append(0)
        f = 1

    for i in range(1,n-1):
        if (a[i]>a[i-1] and a[i]>a[i+1]):
            x.append(i)
            f = 1

    if a[n-1]>a[n-2]:
        x.append(n-1)
        f = 1
    if f == 0:
        print(-1)
    for i in range(len(x)):
        print(x[i], end=' ')
    print()
    t = t - 1