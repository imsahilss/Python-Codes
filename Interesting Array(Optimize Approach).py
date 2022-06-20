t = int(input(''))
while t>0:
    n = int(input(''))
    a = list(map(int, input().split()))
    k = int(input(''))
    i = 0
    j = n-1
    flag = 0
    while(i<j):
        sum = a[i]+a[j]
        if (sum==k):
            flag=1
            print(i,j)
            break
        elif sum>k:
            j = j-1
        else:
            i = i+1

    if flag==0:
        print('no answer')
    t = t-1

