t = int(input(''))
while t > 0:
    n = int(input(''))
    r = list(map(int, input().split()))
    min = r[0]
    x = 0
    for i in range(n):

        if r[i] < min:
            min = r[i]
            x = i

    print(x)
    t -= 1