def patrn(n):
    if (n == 0 or n < 0):
        print(n, end=" ")
        return
    print(n, end=" ")
    patrn(n-5)
    print(n, end=" ")

def main():
    t = int(input())
    while t>0:
        n = int(input())
        patrn(n)
        print()
        t = t-1
if __name__ == '__main__':
    main()

