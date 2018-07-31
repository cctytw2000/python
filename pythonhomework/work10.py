# 10.	請設計一個銀行帳號的類別，有name(姓名)及balance(帳戶餘額)兩個屬性，
# withdraw()提款、deposit()存款及check_balance()檢查餘額的三個方法。
# 產生一個銀行帳號的物件時，請列印出 [Hello Jack, 您的開戶金額是NT$100元]
# 提款時會列印
# 您提了NT$50元
# 餘額NT$50元
# 或
# 您的存款不足

# 存款時會列印出
# 您存了NT$1,000元
# 餘額NT$1,050元


class bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print("Hello {0}, 您的開戶金額是NT${1}元".format(self.name, self.balance))

    def withdraw(self, outmoney):
        if self.balance >= outmoney:
            self.balance -= outmoney
            print("您提了NT${}元餘額NT${}元".format(outmoney, self.balance))
        else:
            print("您的存款不足")

    def deposit(self, inmoney):
        self.balance += inmoney
        print("您存了NT${}元".format(inmoney))

    def check_balance(self):
        print("餘額NT${}元".format(self.balance))


name = input("請輸入姓名:")
makemoney = int(input("請輸入開戶金額:"))
user = bank(name, makemoney)
outmoney = int(input("請輸入提款金額:"))
user.withdraw(outmoney)
while outmoney <= makemoney:
    inmoney = int(input("請輸入存款金額:"))
    user.deposit(inmoney)
    user.check_balance()
    break
