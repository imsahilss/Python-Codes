# def TowerOfHanoi(n,source,destination,helper):
#     if (n==1):
#         print("Move disk from", source, " to ", destination)
#         return
#     TowerOfHanoi(n-1,source,helper,destination)
#     print("Move disk from", source, " to ", destination)
#     TowerOfHanoi(n-1,helper,destination,source)
#
#
#
# n = int(input())
# TowerOfHanoi(n,1,3,2)

t = int(input())
while t>0:
  n = input()
  a = input().split()

  t = t-1

