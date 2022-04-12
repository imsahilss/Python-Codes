# T = int(input(''))
# c = 0
# while T>0:
#     n = int(input(''))
#
#
#     if n%10==0:
#         print(c)
#         c = c+1
#
#
#     elif n%10!=0:
#
#         n=n*2
#         if n%10==0:
#             print(c)
#             c = c+1
#
#         else:
#             print(-1)
#     else:
#         print(-1)
#
#
#     T = T-1
T = int(input(''))
while T>0:
    n = int(input(''))

    if n%10==0:
        print(0)
    elif n%10!=0:
        n = n*2
        if n%10==0:
            print(1)
        else:
            print(-1)
    else:
        print(-1)
    T =T-1