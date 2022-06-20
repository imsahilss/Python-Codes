t=int(input(''))
while t>0:
    n = int(input(''))
    a = list(map(int, input().split()))
    freq = [0]*50
    for i in range(n):
        freq[a[i]] += 1

    for i in range(len(freq)):
        if freq[i]>0:
            print(i,freq[i])

    flag = 0
    for i in range(len(freq)):
        if (freq[i]>1):
            flag = 1
            break
    if flag==1:
        print('Nos are not unique')
    else:
        print('Nos are Unique')

    t-=1