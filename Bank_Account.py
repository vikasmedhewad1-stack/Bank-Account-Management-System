class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.account_no = acc

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount,"was debitted")
        print("total balance :", self.get_balance())

    #creadit method
    def credit(self, amount):
            self.balance += amount
            print("Rs.", amount,"was creditted")
            print("total balance :", self.get_balance())

    #total balance
    def get_balance(self):
         return self.balance

acc1 = Account(10000, 23052005)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(100000)
print(acc1.account_no)