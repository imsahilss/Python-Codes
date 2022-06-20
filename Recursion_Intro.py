def printNum(n):
    if n==0:
         return 0
    print(n)
    printNum(n-1)

def main():
    n = int(input())
    printNum(n)

if __name__ == '__main__':
    main()