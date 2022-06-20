def lowerBound(a,n,tar):
    low = 0
    high = n
    while(low<high):
        mid = (low+high)//2
        if tar<=a[mid]:
            high = mid
        else:
            low = low+1
    return low

def main():
    t = int(input())
    while t>0:
        n = int(input())
        a = list(map(int, input().split()))
        q = int(input())
        while q>0:
            tar = int(input())
            print(lowerBound(a,n,tar))
            q=q-1
        t=t-1

if __name__ == "__main__":
    main()