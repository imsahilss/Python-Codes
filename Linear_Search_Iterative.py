def BinarySearch(a, n, target):
    low = 0
    high = n-1
    while(low<=high):
        mid = low + (high-low)//2

        if (a[mid]==target):
            return mid
        elif (a[mid]<target):
            low = mid+1
        elif (a[mid]<target):
            high = mid-1

    return -1

def main():
    t = int(input())
    while t>0:
        n = int(input())
        a = list(map(int, input().split()))
        target = int(input())
        res = BinarySearch(a,n,target)
        if (res==-1):
            print("Target Value is not present")
        else:
            print("Target value is at index", res)
        t = t-1


if __name__ == "__main__":
    main()
