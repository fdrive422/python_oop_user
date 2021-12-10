class User:
    bank_name = "First National Dojo"
    def __init__(self, name, emailAddress):
        self.name = name
        # self.email = emailAddress
        self.accountBalance = 0

    def makeDepoit(self, amount):
        self.accountBalance += amount

    def makeWithdrawal(self, amount):
        self.accountBalance -= amount

    def displayUserBalance(self):
        print(f"{self.name}, Balance: ${self.accountBalance}")

    def updateEmailAddress(self, newEmailAddress):
        self.email = newEmailAddress

    def transferMoney(self,amount,user):
        self.accountBalance -= amount
        user.accountBalance += amount
        self.displayUserBalance()
        user.displayUserBalance()

tom = User("Tom Cruise", "tom@cruise.com")
pete = User("Pete Mitchell", "pete@maverick.com")
ethan = User("Eathan Hunt", "ethan@imf.com")

tom.makeDepoit(50000)
tom.makeDepoit(100000)
tom.makeDepoit(150000)
tom.makeWithdrawal(25000)
tom.displayUserBalance()

pete.makeDepoit(150000)
pete.makeDepoit(200000)
pete.makeWithdrawal(50000)
pete.makeWithdrawal(150000)
pete.displayUserBalance()

ethan.makeDepoit(300000)
ethan.makeWithdrawal(100000)
ethan.makeWithdrawal(100000)
ethan.makeWithdrawal(50000)
ethan.displayUserBalance()

tom.transferMoney(75000, ethan)