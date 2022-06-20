N = int(input("Enter the no of boxes:"))
c=0
for i in range(1,N+1):
    ti = int(input("Enter the total no of toys in box:"))
    ci = int(input("Enter the capacity of toys in box:"))
    if (ci-ti >= 2):
        print("Yes you can keep in the box")
        c=c+1
    else:
        print("You are not allowed to keep the toys")
print("You can keep the Toys in",c,"Boxes")