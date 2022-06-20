# r = int(input(''))
#
# for i in range(1, r):
#     for k in range(1, r-i):
#         print(" ", end='')
#
#     for j in range(0, 2*i-1):
#         print("*", end='')
#
#     print("")
# otput:
# 6
#     *
#    ***
#   *****
#  *******
# *********

# r = int(input(''))
#
# for i in range(5,0,-1):
#
#     for k in range(1,r-i):
#         print(" ", end='')
#     for j in range(0, 2*i-1):
#         print("*",end='')
#     print("")
# output:
# 6
# *********
#  *******
#   *****
#    ***
#     *

# r = int(input(''))
# n = 1
# for i in range(1, r):
#
#     for j in range(1, i+1):
#         print(n, end='')
#     n += 1
#     print("")
# output:6
#
# 1
# 22
# 333
# 4444
# 55555

# r = int(input(''))
# n = 1
# for i in range(1, r):
#
#     for k in range(1, r-i):
#         print(" ",end='')
#
#     for j in range(1, i+1):
#         print(n, end='')
#     n += 1
#     print("")
#
# output: 6
#
#     1
#    22
#   333
#  4444
# 55555



# r = int(input(''))
# n = 1
# for i in range(1, r):
#
#     for j in range(1, i+1):
#         print(n, end=' ')
#         n += 1
#
#     print("")
#
# output:6
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15



# r = int(input(''))
#
# for i in range(1, r):
#     n = 1
#     for j in range(1, i+1):
#         print(n,end='')
#         n = n+1
#     print("")
#
# output:6
#
# 1
# 12
# 123
# 1234
# 12345

spaces = 8
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end='')
    for k in range(1, spaces+1):
        print(" ", end='')
    spaces -= 2
    for j in range(i, 0, -1):
        print(j, end='')
    print("")
































