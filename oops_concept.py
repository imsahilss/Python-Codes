# class Mobile:
#     def __init__(self):
#         self.brandname = "Samsung"
#         self.color = "Black"
#         self.isJack = False
#     def calling(self):
#         print('Calling')
#     def cameraclick(self):
#         print('Picture Captured')
#     def message(self):
#         print('Message sent')
#
# def main():
#     m1 = Mobile()
#     print(m1.brandname)
#     print(m1.color)
#     print(m1.isJack)
#     m1.calling()
#     m1.cameraclick()
#     m1.message()
#     print('-----------------------')
#     m2 = Mobile()
#     m2.cameraclick()
#
#
#
#
#
# if __name__ == '__main__':
#     main()



class Mobile:
    def __init__(self, bN, color, isJack):
        self.brandname = bN
        self.color = color
        self.isJack = isJack
    def calling(self):
        print('Calling')
    def cameraclick(self):
        print('Picture Captured')
    def message(self):
        print('Message sent')

def main():
    m1 = Mobile("Apple", "White", True)
    print(m1.brandname)
    print(m1.color)
    print(m1.isJack)
    m1.calling()
    m1.cameraclick()
    m1.message()
    print('-----------------------')
    m2 = Mobile("MI", "Rose-Red", False)
    print(m2.brandname)
    print(m2.color)
    print(m2.isJack)
    m2.calling()
    m2.cameraclick()
    var = 365
    print(var.bit_length())
    print()





if __name__ == '__main__':
    main()
