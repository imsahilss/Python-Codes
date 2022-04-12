def ArrZigZag(n,a):
    e = 0
    o = 0
    f = -1
    s = -1
    for i in range(0,n+1):
        if (i+1<n):
            if (f == -1 and s == -1):
                f = a[i]
                s = a[i+1]
            else:
                s = a[i+1]
            if (i%2==0):
                if(f<=s):
                    d = s-f
                    e += d+1
                    s = s-(d+1)
            else:
                if(f>=s):
                    d = f-s
                    e += d+1
                    f = f-(d+1)
    f = -1
    s = -1

    for i in range(1,n+1):
        if (i+1<n):
            if (f == -1 and s == -1):
                f = a[i]
                s = a[i+1]
            else:
                s = a[i+1]
            if (i):
                if(f>=s):
                    d = f-s
                    o += d+1
                    f = f-(d+1)
            else:
                if(f<=s):
                    d = s-f
                    o += d+1
                    s = s-(d+1)
    print(min(e,o)-1)

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ArrZigZag(n,a)

if __name__=='__main__':
    main()
