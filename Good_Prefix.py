t = int(input())
while t!=0:
    st = input()
    k,x = map(int, input().split())
    c = 0
    freq = [0]*26
    for i in range(len(st)):
        ele = ord(st[i])-97
        freq[ele]+=1
        if(freq[ele]>x):
            if(k>0):
                freq[ele]-=1
                k -=1
            else:
                break
        else:
            c=c+1
    print(c)
    t = t-1

