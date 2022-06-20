# wa, a = map(int, input().split())
# if wa%5 == 0:
#     a = a-wa-0.5
#     print(a)
# elif wa>a:
#     print(a)
# elif wa%5 != 0:
#     print(a)

# t = int(input(''))
# while t>0:
#     a = list(map(int, input().split()))
#
#     if (7 in a):
#         print('Yes')
#     else:
#         print('No')
#     t = t-1

T = int(input(''))
x, y, z = 0, 0, 0
while (T > 0):
    R = list(map(int, input().split()))

    for i in range(len(R)):
        if R[i] == 0:

            x = x+1
        elif R[i] == 1:

            y = y+1
        elif R[i] == 2:

            z = z+1

    if ((x > y and x > z and y==z)):
        print('Draw')
    elif (y > z and y > x):
        print('India')
    elif (z > y and z > x):
        print('England')
    T -= 1