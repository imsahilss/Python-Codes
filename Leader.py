t = int(input(''))
while t>0:
  n = int(input(''))
  a = list(map(int, input().split()))
  x = []
  max = 0
  for i in range(n-1,-1,-1):
    if (a[i]>=max):
      max = a[i]
      x.append(a[i])

  x.sort()
  for i in range(len(x)):
    print(x[i], end=' ')
  print()
  t = t-1


