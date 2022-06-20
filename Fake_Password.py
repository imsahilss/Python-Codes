t = int(input(''))
while t>0:
    org = input('')
    fake = input('')
    lf = fake[0:2]
    lr = fake[2:]
    left = lr+lf
    rf = fake[len(fake)-2:]
    rr = fake[0:len(fake)-2]
    right = rf + rr
    if (org==left or org==right):
        print("Yes")
    else:
        print("No")
    t=t-1

