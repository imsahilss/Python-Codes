class Account:
    __amount = 0
    def deposit(self,add):
        self.__amount += add

    def debit(self,sub):
        self.__amount -= sub

    def printAmount(self):
        print(self.__amount)


b1 = Account()
b1.deposit(1000)
#b1.printAmount()
b1.debit(750)
b1.debit(7.5)
b1.printAmount()
