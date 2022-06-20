# def UpperBound(a,n,tar):
#     low = 0
#     high = n
#     while(low<high):
#         mid = (low+high)//2
#         if tar>=a[mid]:
#             low = mid+1
#         else:
#             high = mid
#     return low
#
# def main():
#     t = int(input())
#     while t>0:
#         n = int(input())
#         a = list(map(int, input().split()))
#         q = int(input())
#         while q>0:
#             tar = int(input())
#             print(UpperBound(a,n,tar))
#             q=q-1
#         t=t-1
#
# if __name__ == "__main__":
#     main()


def UpperBound(a,n,tar):
    low = 0
    high = n
    f = 0
    while(low<high):
        mid = (low+high)//2
        if tar<=a[mid]:
            high = mid
        else:
            low = mid
    return low

def main():
    t = int(input())
    while t>0:
        n ,k= map(int,input().split())
        a = list(map(int, input().split()))
        print(UpperBound(a,n,k))

        t=t-1

if __name__ == "__main__":
    main()