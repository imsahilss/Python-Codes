def main():
    t = int(input())
    while(t!=0):
        n = int(input())
        arr = list(map(int,input().split()))
        span = [1]*n
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if(arr[i]>=arr[j]):
                    span[i]+=1
                else:
                    break
        for ele in span:
            print(ele, end=' ')
        print()

if __name__ == '__main__':
    main()