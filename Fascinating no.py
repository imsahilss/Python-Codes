T = int(input(''))
while T > 0:
    N = int(input(''))
    f = 0
    t = 0
    while (f == 0):
        N += 1
        t = N
        a = t % 10
        t = t // 10
        b = t % 10
        t = t // 10
        c = t % 10
        t = t // 10
        d = t % 10

        if ((a != b and a != c and a != d) and (b != c and b != d) and (c != d)):
            f = f + 1
    print(N)
    T -= 1
