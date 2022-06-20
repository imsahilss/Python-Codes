t = int(input(''))
while(t>0):
        n,k = map(int, input().split())
        a = list(map(int, input().split()))
        s = 0

        for i in range(0, k):
            s = s+a[i]
        max = s
        for i in range(k, n):
            s = s-a[i-k]+a[i]
            if max<s:
                max=s

        print(max)
        t = t-1