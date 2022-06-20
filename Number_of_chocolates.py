def UpperBound(x,n,tar):
    low = 0
    high = n
    while(low<high):
        mid = (low+high)//2
        if tar>=x[mid]:
            low = mid+1
        else:
            high = mid
    return low

def main():

    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    x = a[::-1]
    while q>0:
        tar = int(input())
        print(UpperBound(x,n,tar))
        q=q-1


if __name__ == "__main__":
    main()