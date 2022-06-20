T = int(input(''))
while T>0:
    N = int(input(''))
    a = N%8

    if a==0:
        print(str(int(N-1))+'SL')
    elif a==1:
        print(str(int(N+3)) + 'LB')
    elif a==2:
        print(str(int(N+3)) + 'MB')
    elif a==3:
        print(str(int(N+3)) + 'UB')
    elif a==4:
        print(str(int(N-3)) + 'LB')
    elif a==5:
        print(str(int(N-3)) + 'MB')
    elif a==6:
        print(str(int(N-3)) + 'UB')
    elif a==7:
        print(str(int(N+1)) + 'SU')
    T = T-1
