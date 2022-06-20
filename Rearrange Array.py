t = int(input(''))
while t>0:
  n = int(input(''))
  a = list(map(int, input().split()))
  x = []
  s = 0
  e = n-1
  for i in range(0,n):
      if i%2==0:
          x.append(a[e])
          e = e - 1
      else:
          x.append(a[s])
          s = s+1
  for i in range(len(x)):
      print(x[i], end=' ')
  print(" ")
  t = t-1
















