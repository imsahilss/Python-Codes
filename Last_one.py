t = int(input(''))
while t > 0:
    n = int(input(''))
    a = list(map(int, input().split()))
    d = 0
    for i in range(n):
        d = d+a[i]
        if d == 0:
            c = -1
        else:
            if a[i]==1:
                c = i

    print(c)


    t = t - 1