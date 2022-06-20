n = int(input(''))
a = list(map(int, input().split()))
freq = [0]*121
c = 0
for i in range(n):
    freq[a[i]] += 1

for i in range(len(freq)):
    for j in range(len(freq)):
        if (i<= 0.5*j+7):
            continue
        if (i>100 and j<100):
            continue
        if (i>j):
            continue
        c += freq[i]*freq[j]
        if(i==j):
            c -= freq[i]
print(c)
