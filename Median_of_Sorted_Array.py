def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    mid = int((n-1)/2)
    for i in range(n):
       if ((n-1)%2==0):
           median = arr[mid]


       else:
           median = arr[mid+1]
    print(median)

if __name__ == '__main__':
    main()
