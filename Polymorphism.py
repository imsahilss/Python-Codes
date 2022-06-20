class jiocaller():
    def call(self):
        print("Calling")

class truecaller():
    def call(self):
        print("Ringing")
        print("Caller Data")

class Phone:
    def callFunc(self, phoneApp):
        phoneApp.call()

phoneApp = jiocaller()
p1 = Phone()
p1.callFunc(phoneApp)