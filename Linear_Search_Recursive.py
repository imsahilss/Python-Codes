def Recursive_BinarySearch(a, low, high, target):
    if low>high:
        return -1
    mid = low + (high - low) // 2

    if (a[mid] == target):
        return mid
    elif (a[mid]<target):
        return Recursive_BinarySearch(a, mid+1, high, target)
    elif (a[mid]>target):
        return Recursive_BinarySearch(a, low, mid-1, target)

def main():
    t = int(input())
    while t>0:
        n = int(input())
        a = list(map(int, input().split()))
        target = int(input())
        res = Recursive_BinarySearch(a,0,n-1,target)
        if (res==-1):
            print("Target Value is not present")
        else:
            print("Target value is at index", res)
        t = t-1


if __name__ == "__main__":
    main()