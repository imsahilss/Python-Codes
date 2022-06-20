# a = int(input())
# b = int(input())
#
# try:
#     print(a // b)
# except Exception as e:
#     print(e)

# a = int(input())
# b = input()
# try:
#     print(a + c)
# except Exception as e:
#     print(e)

arr = [1, 2, 3, 4, 5]
try:
    a = int(input())
    print(arr[3])

except Exception as e:
    print(e)

finally:
    print("Printing")