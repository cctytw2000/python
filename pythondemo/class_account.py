class Account:
    count = 0
    def __init__(self, id, name):
        self.account_id = id
        self.account_name = name
        self.__balance = 0
        Account.count += 1
    
    def deposite(self, amount):
        if amount <= 0:
            raise ValueError("最少要一塊")
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise RuntimeError("餘額不足")

    def show(self):
        return self.__balance;

userA = Account("a123455667","Jack");
userB = Account("a123454321","Mary");
userC = Account("a122233344","Tom");
print("客戶人數：{}".format(Account.count))
# userA.deposite(0)
# userA.withdraw(1500)
# userA.__balance = 1000
# print(userA.__balance)
# userA.deposite(500)
# userA.withdraw(100)
# print(userA.show())


