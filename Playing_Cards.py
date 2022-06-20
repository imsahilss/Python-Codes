# t = int(input())
# while t > 0:
#     n = input()
#     a = input().split()
#     c = 0
#     for i in range(len(a)):
#       if n in a[i]:
#         c = 1
#         break
#       elif n[0:1] in a[i]:
#         c = 1
#         break
#       elif n[1:] in a[i]:
#         c = 1
#         break
#       else:
#         c = 0
#     if c==1:
#       print('Yes')
#     else:
#       print('No')
#     t = t-1

t = int(input())
while t>0:
    n = input()
    for i in n:
        x = max(ord(n[i]))
        str = x + 























