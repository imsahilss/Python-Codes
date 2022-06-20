T = int(input(''))

while T>0:
    N = int(input(""))
    sum = 0
    for i in range(1,N):

        if(N%i==0):
            sum = sum+i




    if sum==N:
        print("true")
    else:
        print("false")

    T = T-1
