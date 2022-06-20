def main():
    t = int(input(''))
    while(t>0):
        n,k = map(int, input().split())
        a = list(map(int, input().split()))

        m = -1
        for i in range(0, n-k+1):
            s = 0
            for j in range(i,i+k):
                s = s+a[j]
            if s>m:
                m = s
        print(m)
        t = t-1

if __name__ == '__main__':
    main()

