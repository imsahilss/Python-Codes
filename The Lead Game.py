n = int(input(''))
p1 = 0
p2 = 0
lead = 0
for i in range(n):
    s1 , s2 = map(int, input().split())
    p1 = p1 + s1
    p2 = p2 + s2
    d = p1-p2
    if d>0 and d>lead:
        lead = d
        l = 1
    elif d<0 and abs(d)>lead:
        lead = d
        l = 2
print(l, lead)