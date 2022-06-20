# a = 5
# b = 7
# # print(a&b)
# # print(a|b)
# # print(~a)
# # print(~b)
#
# print(1<<1)
# print(3<<2)
# print(4<<3)
# print(4>>1)
# print(4>>2)
# print(16>>2)


# #Set the Kth Bits
# n,k = map(int, input().split())
# n = n | (1<<k)
# print(n)
# print(bin(n))
# print("\n")
#
# #UnSet the Kth Bits
# n,k = map(int, input().split())
# n = n & ~(1<<k)
# print(n)
# print("\n")

#Toggle
n,k = map(int, input().split())
n = n ^ (1<<k)
print(n)
print(bin(107))
print(bin(123))

if (n & (1<<k)!=0):
    print("Kth bit is set")
else:
    print("Kth bit is unset")






