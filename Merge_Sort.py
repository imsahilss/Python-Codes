def merge(arr,l,mid,r):
    n = mid-l+1
    m = r-mid
    arr_1 = [0]*n
    arr_2 = [0]*m
    for i in range(n):
        arr_1[i]=arr[l+i]
    for i in range(m):
        arr_2[i]=arr[mid+1+i]

    i = 0
    j = 0
    k = l

    while(i<n and j<m):
        if (arr_1[i]<arr_2[j]):
            arr[k] = arr_1[i]
            k = k+1
            i = i+1
        else:
            arr[k] = arr_2[j]
            k = k + 1
            j = j + 1
    while(i<n):
        arr[k] = arr_1[i]
        k = k+1
        i = i+1

    while (j < m):
        arr[k] = arr_2[j]
        k = k + 1
        j = j + 1

def mergeSort(arr,l,r):
    if(l<r):
        mid = l+(r-l)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)

def main():
    t = int(input())
    while t>0:
        p = int(input())
        arr = list(map(int, input().split()))
        mergeSort(arr,0,p-1)
        for i in range(p):
            print(arr[i], end=' ')
        print()
        t = t-1

if __name__=='__main__':
    main()
