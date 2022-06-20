def sumOfN(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return n + sumOfN(n-1)
def main():
    n = int(input())
    print(sumOfN(n))

if __name__ == '__main__':
    main()