class Account:
    _amount = 0
    def deposit(self,add):
        self._amount += add

    def debit(self,sub):
        self._amount -= sub

    def printAmount(self):
        print(self._amount)


class User(Account):
    def calculateTax(self):
        tax = self._amount*0.2
        print(tax)



u1 = User()
u1.deposit(1000)
u1.printAmount()
u1.debit(448)
u1.printAmount()
u1.calculateTax()
