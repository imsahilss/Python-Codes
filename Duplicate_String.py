t = int(input(''))
while t>0:
    str = input('')

    freq = [0]*26
    for i in range(len(str)):
        freq[ord(str[i]) - 97] += 1


    f=0
    for i in range(len(str)):
        if freq[i]>-1:
            print("{}{}".format(chr(i+97),freq[str]),end=' ')
            f = 1
    if f==0:
        print(-1)
    else:
        print()

    t = t-1
