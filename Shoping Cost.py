N = int(input(''))
while N > 0:
    q, p = map(int, input().split())
    r = q * p
    if (q > 100):
        r = r * 0.8
        print("%.1f" % (r))
    else:
        print("%.1f" % (r))

    N -= 1