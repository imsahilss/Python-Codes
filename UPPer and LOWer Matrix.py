n,m = map(int, input().split())
mat1 = []
for i in range(n):
    mat1.append(list(map(int, input().split())))

for i in range(0, n):
    for j in range(0, m):
        if (i < j):
            print("0", end=" ")
        else:
            print(mat1[i][j], end=" ")
    print(" ")
for i in range(0, n):
    for j in range(0, m):
        if (i > j):
            print("0", end=" ")
        else:
            print(mat1[i][j], end=" ")
    print(" ")



