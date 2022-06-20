def fact(n):
    if n<0:
        return 0
    elif n==1 or n==0:
        return 1
    return n*fact(n-1)
def main():
    t = int(input())
    while t>0:

        n = int(input())
        print(fact(n))
        t = t-1

if __name__ == '__main__':
    main()