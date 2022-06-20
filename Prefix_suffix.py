t = int(input())
while t>0:
    n = input('')
    for i in range(1,len(n)+1):
        a = n[:i]
        print(a)
    for j in range(1,len(n)+1):
        a=n[-j:]
        print(a)
    print()
    t=t-1