T = int(input(''))
while T>0:
    N = int(input(''))
    a = list(map(int, input().split()))
    max = -1
    min = 10**9
    for i in range(N):
        if a[i]<min:
            min = a[i]
        if a[i]>max:
            max = a[i]
    print(min, max)
    T -= 1
