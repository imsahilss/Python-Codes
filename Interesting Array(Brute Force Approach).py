t =int(input(''))
while t>0:
    n = int(input(''))
    a = list(map(int, input().split()))
    k = int(input(''))
    min_i = -1
    max_j = -1
    flag = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if (a[i]+a[j]==k):
                flag=1
                if j>max_j:
                    min_i = i
                    max_j = j
                elif (max_j==j and min_i>i):
                    min_i = i
                    max_j = j
    if flag == 0:
        print('no answer')
    else:
        print(min_i,max_j)

    t-=1