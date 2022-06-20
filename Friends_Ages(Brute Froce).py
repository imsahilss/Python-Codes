n = int(input(''))
a = list(map(int, input().split()))
c = 0
for i in range(n):

    for j in range(n):
        if i!=j:
            if a[j]<= 0.5*a[i]+7:
                continue
            elif (a[j]>100 and a[i]<100):
                continue
            elif a[j]>a[i]:
                continue
            else:
                c = c+1
print(c)

