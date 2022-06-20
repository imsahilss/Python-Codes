'''Among all the digits from 0−9, PrepBuddy likes number 5. He has lots of numbers and wants you to find out the number of times
5 occurred in each number.
Input format
The first line contains an integer T denoting the number of test cases.
Each of the next T lines contains a single integer N.
'''

T = int(input(''))

while T>0:
    c = 0
    N = int(input(''))
    while N>0:

        r = N%10
        if r==5:
            c += 1
        N = N//10
    T -= 1
    print(c)