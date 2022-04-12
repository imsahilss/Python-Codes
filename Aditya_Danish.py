# t = int(input())
# while t > 0:
#     n = int(input())
#     s = input('')
#     a = 0
#     d = 0
#     for i in range(n):
#
#         if s[i] == 'A':
#             a += 1
#         else:
#             d += 1
#
#     if a > d:
#         print('Aditya')
#     elif d > a:
#         print('Danish')
#     elif a == d:
#         print('AdiDan')
#
#     t = t - 1

t = int(input())
while t > 0:
    s = input('')
    v = 0
    c = 0
    for i in s:
        if (i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            v = v + 1
        else:
            c = c + 1

    print(v, c)
    t = t - 1