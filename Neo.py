# def test(i,j):
#     if(i==0):
#         return j
#     else:
#         return test(i-1,i+j)
# print(test(4,7))


# def f1():
#     x=100
#     print(x)
# x=+1
# f1()


# def doSomething(a, b):
#  if (b==1):
#     return a
#  else:
#     return a + doSomething(a,b-1)
# print(doSomething(2,3))
# def fun(n):
#     if (n > 100):
#         return n - 5
#     return fun(fun(n + 11))
#
#
# print(fun(45))
#
# l=[]
# def convert(b):
#     if(b==0):
#         return l
#     dig=b%2
#     l.append(dig)
#     convert(b//2)
# convert(6)
# l.reverse()
# for i in l:
#     print(i,end="")

# def f(n):
#   if n >1:
#    print('Still printing')
#    f(n/2)
# f(32)
# def prints(n):
#   if(n == 0):
#     return
#   print(n%2,end='')
#   prints(n//2)
#
# prints(12)

# def a(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return a(n-1)+a(n-2)
# for i in range(0,4):
#     print(a(i),end=" ")

# def func(a, b):
#     if(b==0):
#         return 0
#     if(b==1):
#         return a
#     return a + func(a,b-1)
# print(func(3,8))

def a(n):
    if n == 0:
        return 0
    else:
        return n*a(n - 1)
def b(n, tot):
    if n == 0:
        return tot
    else:
        return b(n-2, tot-2)