# n = int(input(""))
# r = 0
# while n>0:
#     d = n%10
#     r = r*10 + d
#     n = n//10
#
# first_digit = r%10
# print(first_digit)

n = int(input(''))
r = 0
while(n>0):
    r = n%10
    n = n//10
print(r)