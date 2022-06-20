n = int(input(''))
a = list(map(int, input().split()))
e = []
o = []
for i in range(n):
    if a[i] % 2 == 0:
        e.append(a[i])

    else:
        o.append(a[i])

for j in range(len(e)):
  print(e[j], end=' ')
print(("\r"))
for k in range(len(o)):
  print(o[k], end=' ')
