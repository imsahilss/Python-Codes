# a = []
# for ele in input().split():
#     a.append(int(ele))
#
# for i in range(len(a)):
#     print(a[i],end = ' ')

a = list(map(int, input().split()))
for i in range(len(a)):
    print(a[i],end=" ")
