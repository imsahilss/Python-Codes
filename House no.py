t=int(input())
while(t>0):
    n=int(input())
    d=0
    i=1
    while(i<=n):
        d+=n-i+1
        i=i*10
    print(d)
    t=t-1