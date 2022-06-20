r = int(input(""))

for i in range(r):
    print(" "*(r-i-1)+"* "*(i+1))
for j in range(r-1,0, -1):
    print(" "*(r-j)+"* "*(j))
